from odoo import http
from odoo.http import request
from datetime import datetime


class GetQuizData(http.Controller):

    @http.route('/get/grid_question_data', type='json',
                website=True, auth='user', csrf=False)
    def change_grid_question_data(self, **post):
        result_line = request.env['op.quiz.result'].sudo().browse(
            int(post.get('result_id')))
        quiz = request.env['op.quiz.result'].sudo().search_read(
            [('id', '=', int(post.get('result_id')))], [])
        quiz_data = request.env['op.quiz'].sudo().search_read(
            [('id', '=', result_line.quiz_id.id)], [])
        question_no = 1
        for record in quiz:
            last = record['line_ids']
            last_que = last[-1]
        for value in result_line.line_ids:
            if post.get('current_que') == value.id:
                if post.get('answer'):
                    value.given_answer = post.get('answer')
        for value in result_line.line_ids:
            if post.get('que_id') == value.id:
                next_que = request.env['op.quiz.result.line'].sudo().search_read(
                    [('id', '=', value.id)], [])
                next_que_resu = request.env['op.quiz.result.line'].\
                    sudo().search([('id', '=', value.id)])
                line_ids = {}
                for answer in value.line_ids:
                    if answer.name == value.given_answer:
                        line_ids[answer.name] = True
                    else:
                        line_ids[answer.name] = False
                for data in next_que:
                    data['line_ids'] = line_ids
                    data['embed_code'] = value.bank_line.embed_code
                    data['given_answer'] = value.given_answer
                    data['question_no'] = question_no
                    data['total_question'] = len(result_line.line_ids)
                    multiple_choice_line_ids = []
                    if 'multiple_choice_line_ids' in data:
                        for multiple_choice_id in \
                                next_que_resu.multiple_choice_line_ids:
                            if data['multiple_choice_que_type'] == 'text':
                                multiple_choice_line_ids.append(
                                    {'id': multiple_choice_id.id,
                                     'que_text': multiple_choice_id.que_text})
                            if data['multiple_choice_que_type'] == 'image':
                                multiple_choice_line_ids.append(
                                    {'id': multiple_choice_id.id,
                                     'que_image': multiple_choice_id.que_image})
                        data['multiple_choice_line_ids'] = multiple_choice_line_ids
                    if value.id == last_que:
                        data['last_que'] = True
                    else:
                        data['last_que'] = False
                return {'next_que': next_que, 'quiz': quiz_data[0]}
            question_no = question_no + 1

    @http.route('/get/quiz-data', type='json', website=True, auth='user', csrf=False)
    def get_next_quiz_data(self, **post):
        result_line = request.env['op.quiz.result'].sudo().browse(
            int(post.get('result_id')))
        quiz = request.env['op.quiz.result'].sudo().search_read(
            [('id', '=', int(post.get('result_id')))], [])
        quiz_data = request.env['op.quiz'].sudo().search_read(
            [('id', '=', result_line.quiz_id.id)], [])
        question_no = 1
        for record in quiz:
            last = record['line_ids']
            last_que = last[-1]
        temp = 0
        for value in result_line.line_ids:
            if temp == 1:
                next_que = request.env['op.quiz.result.line'].sudo().search_read(
                    [('id', '=', value.id)], [])
                next_que_resu = request.env['op.quiz.result.line'].\
                    sudo().search([('id', '=', value.id)])
                line_ids = {}
                for answer in value.line_ids:
                    if answer.name == value.given_answer:
                        line_ids[answer.name] = True
                    else:
                        line_ids[answer.name] = False
                for data in next_que:
                    data['line_ids'] = line_ids
                    data['embed_code'] = value.bank_line.embed_code
                    data['given_answer'] = value.given_answer
                    data['question_no'] = question_no
                    data['total_question'] = len(result_line.line_ids)
                    multiple_choice_line_ids = []
                    if 'multiple_choice_line_ids' in data:
                        for multiple_choice_id in \
                                next_que_resu.multiple_choice_line_ids:
                            if data['multiple_choice_que_type'] == 'text':
                                multiple_choice_line_ids.append(
                                    {'id': multiple_choice_id.id,
                                     'que_text': multiple_choice_id.que_text})
                            if data['multiple_choice_que_type'] == 'image':
                                multiple_choice_line_ids.append(
                                    {'id': multiple_choice_id.id,
                                     'que_image': multiple_choice_id.que_image})
                        data['multiple_choice_line_ids'] = multiple_choice_line_ids
                    if value.id == last_que:
                        data['last_que'] = True
                    else:
                        data['last_que'] = False
                return {'next_que': next_que, 'quiz': quiz_data[0]}
            if post.get('que_id') == value.id:
                if post.get('answer'):
                    value.given_answer = post.get('answer')
                temp = 1
            question_no = question_no + 1

        if temp == 0:
            return False

    @http.route('/get/prev-question-data', type='json',
                website=True, auth='user', csrf=False)
    def get_prev_quiz_data(self, **post):
        result_line = request.env['op.quiz.result'].sudo().browse(
            int(post.get('result_id')))
        quiz = request.env['op.quiz.result'].sudo().search_read(
            [('id', '=', int(post.get('result_id')))], [])
        quiz_data = request.env['op.quiz'].sudo().search_read(
            [('id', '=', result_line.quiz_id.id)], [])
        question_no = 1
        prev_que = None
        for record in quiz:
            last = record['line_ids']
            last_que = last[-1]
        for value in result_line.line_ids:
            if post.get('que_id') == value.id:
                next_que = request.env['op.quiz.result.line'].sudo().search_read(
                    [('id', '=', prev_que.id)], [])
                next_que_resu = request.env['op.quiz.result.line'].\
                    sudo().search([('id', '=', value.id)])
                line_ids = {}
                for answer in prev_que.line_ids:
                    if answer.name == prev_que.given_answer:
                        line_ids[answer.name] = True
                    else:
                        line_ids[answer.name] = False
                if post.get('answer'):
                    value.given_answer = post.get('answer')
                for data in next_que:
                    data['line_ids'] = line_ids
                    data['embed_code'] = prev_que.bank_line.embed_code
                    data['given_answer'] = prev_que.given_answer
                    data['question_no'] = question_no - 1
                    data['total_question'] = len(result_line.line_ids)
                    multiple_choice_line_ids = []
                    if 'multiple_choice_line_ids' in data:
                        for multiple_choice_id in \
                                next_que_resu.multiple_choice_line_ids:
                            if data['multiple_choice_que_type'] == 'text':
                                multiple_choice_line_ids.append(
                                    {'id': multiple_choice_id.id,
                                     'que_text': multiple_choice_id.que_text})
                            if data['multiple_choice_que_type'] == 'image':
                                multiple_choice_line_ids.append(
                                    {'id': multiple_choice_id.id,
                                     'que_image': multiple_choice_id.que_image})
                        data['multiple_choice_line_ids'] = multiple_choice_line_ids
                    if prev_que.id == last_que:
                        data['last_que'] = True
                    else:
                        data['last_que'] = False
                return {'next_que': next_que, 'quiz': quiz_data[0]}
            prev_que = value
            question_no = question_no + 1

    @http.route('/get/first_que/quiz-data', type='json',
                website=True, auth='user', csrf=False)
    def get_first_question_data(self, **post):
        result_line = request.env['op.quiz.result'].sudo().browse(
            int(post.get('result_id')))
        quiz_data = request.env['op.quiz'].sudo().search_read(
            [('id', '=', result_line.quiz_id.id)], [])
        for value in result_line.line_ids:
            next_que = request.env['op.quiz.result.line'].sudo().search_read(
                [('id', '=', value.id)], [])
            next_que_resu = request.env['op.quiz.result.line'].\
                sudo().search([('id', '=', value.id)])
            line_ids = {}
            for answer in value.line_ids:
                if answer.name == value.given_answer:
                    line_ids[answer.name] = True
                else:
                    line_ids[answer.name] = False
            for data in next_que:
                data['line_ids'] = line_ids
                data['given_answer'] = value.given_answer
                data['embed_code'] = value.bank_line.embed_code
                data['total_question'] = len(result_line.line_ids)
                data['question_no'] = 1
                multiple_choice_line_ids = []
                if 'multiple_choice_line_ids' in data:
                    for multiple_choice_id in next_que_resu.multiple_choice_line_ids:
                        if data['multiple_choice_que_type'] == 'text':
                            multiple_choice_line_ids.append(
                                {'id': multiple_choice_id.id,
                                 'que_text': multiple_choice_id.que_text})
                        if data['multiple_choice_que_type'] == 'image':
                            multiple_choice_line_ids.append(
                                {'id': multiple_choice_id.id,
                                 'que_image': multiple_choice_id.que_image})
                    data['multiple_choice_line_ids'] = multiple_choice_line_ids
            return {'next_que': next_que, 'quiz': quiz_data[0],
                    'state': result_line.state}

    @http.route('/quiz/attempt-record', type="json", auth="public", sitemap=False,
                website=True)
    def quiz_result_attempt(self, **post):
        result = request.env['op.quiz.result'].sudo().browse(
            int(post.get('result_id')))
        for value in result.line_ids:
            if post.get('que_id') == value.id:
                if post.get('answer'):
                    value.given_answer = post.get('answer')
            value = result.get_answer_data()
        result.write({
            'state': 'submit',
            'submit_date': datetime.today(),
        })

    @http.route('/quiz/attempt/record/submit/<int:result_id>',
                type="http", auth="public", sitemap=False, website=True, csrf=False)
    def quiz_result_attempt_submit(self, result_id=None, **post):
        result = request.env['op.quiz.result'].sudo().browse(int(result_id))
        for value in result.line_ids:
            value = result.get_answer_data()
        if not result.quiz_id.show_result:
            return http.request.render('openeducat_quiz.quiz_completed', {})
        return http.request.render('openeducat_quiz.quiz_results', value)
