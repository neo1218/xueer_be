# coding: utf-8
"""
评论API模块

     评论的资源比较特殊，所有评论堆在一起是对我们毫无益处的
     评论需要依托其赋予的对象的实体，在学而中就是课程
     当然评论的创造者 用户 也是重要的一块资源

         用户 ---> 评论 ---> 课程
"""

from flask import request, jsonify, url_for, current_app, g
from .. import db
from flask_login import current_user
from ..models import Comments, Courses, User, Permission
from . import api
from .decorators import permission_required
import json

@api.route('/courses/<int:id>/comments/', methods=['GET'])
def get_courses_id_comments(id):
    """
    获取特定id课程的评论
    :param id: 课程的id
    :return: 评论json数据
    """
    course = Courses.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = course.comment.order_by(Comments.time.asc()).paginate(
        page, per_page=current_app.config['XUEER_COMMENTS_PER_PAGE'],
        error_out=False
    )
    comments = pagination.items
    prev = ""
    if pagination.has_prev:
        prev = url_for('api.get_comments', page=page - 1, _external=True)
    next = ""
    if pagination.has_next:
        next = url_for('api.get_comments', page=page + 1, _external=True)
    comments_count = len(Comments.query.filter_by(course_id=id).all())
    page_count = comments_count//current_app.config["XUEER_COMMENTS_PER_PAGE"] + 1
    last = url_for('api.get_courses_id_comments', id=id, page=page_count, _external=True)
    return json.dumps(
        [comment.to_json() for comment in comments],
        ensure_ascii=False,
        indent=1
    ), 200, {'Link': '<%s>; rel="next", <%s>; rel="last"' % (next, last)}


@api.route('/courses/<int:id>/comments/hot/', methods=["GET"])
def get_hot_comments(id):
    """
    获取特定id课程的热门评论(以3作为热门鉴定)
    :param id: 课程id
    :return: 评论 json 数据
    """
    comments_dict = {}  # 存取键值: {评论: 点赞数}
    course = Courses.query.get_or_404(id)  # 获取这个id课程
    comments = Comments.query.filter_by(course_id=id).all()  # 该课程对应评论的时间列表(默认按id排序)
    for comment in comments:
        if comment.user.count() >= 3:
            comments_dict[comment] = comment.user.count()
    # 按点赞数从大到小排序
    sorted(comments_dict.items(), lambda x, y: cmp(y[1], x[1]))
    # 获取最热评论列表
    hot_comments = []
    for item in comments_dict:
        hot_comments.append(item)
    return json.dumps(
        [comment.to_json() for comment in hot_comments],
        ensure_ascii=False,
        indent=1
    ), 200


@api.route('/courses/<int:id>/comments/', methods=['POST', 'GET'])
# @permission_required(Permission.COMMENT)
def new_comment(id):
    """
    向特定id的课程发布一个评论
    :param id: 课程id
    :return:
    """
    comment = Comments.from_json(request.json)
    comment.author = g.current_user
    comment.course_id = id
    db.session.add(comment)
    db.session.commit()
    return jsonify(
        comment.to_json()), 201, {
               'Location': url_for(
                    'api.get_courses_id_comments',
                    id=id, _external=True
               )
           }


@api.route('/comments/<int:id>/', methods=["GET", "DELETE"])
def delete_comment(id):
    """
    删除一个评论
    :param id:
    :return:
    """
    comment = Comments.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({
        'message': '该评论已经被删除'
    })


@api.route('/comments/<int:id>/like/', methods=['PUT', 'GET'])
# @permission_required(Permission.COMMENT)
def comment_like(id):
    """
    对特定id的评论点赞
    :param id:
    :return:
    """
    comment = Comments.query.get_or_404(id)
    user = User.query.filter_by(id=g.current_user.id).first()
    comment.user.all().append(user)
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_json()), 200
