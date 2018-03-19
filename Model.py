from base import BOJObject
import types

class Group(BOJObject):
    __slots__ = ['idx', 'name', 'description']
    __types__ = {"idx":types.IntType, "description":types.StringType, "name":types.StringType}
    def __init__(self, idx=0, name='', description=''):
        self.idx = idx
        self.name = name
        self.description = description

        self._id_attrs = (self.idx, )
class User(BOJObject):
    #is id == unique?
    __slots__ = ['username', 'description', 'rank', 'solved', 'submitted', 'workbook_cleared', 'solution_written', 'contest_first', 'contest_second', 'problem_created', 'problem_translated', 'problem_foundtypo', 'problem_foundmistake_data', 'problem_foundmistake_condition', 'problem_adddata', 'problem_found_noncecondition', 'problem_foundwrongtranslation', 'problem_createddata','problem_createspecialjudge','accepted', 'wrong_output', 'wrong', 'tle', 'mle',
    'output_exceed', 'runtime', 'compile', 'school']
    __types__ = {"username":types.StringType,
            "description":types.StringType,
            "rank":types.IntType,
            "solved":types.IntType,
            "submitted":types.IntType,
            "workbook_cleared":types.IntType,
            "solution_written":types.IntType,
            "contest_first":types.IntType,
            "contest_second":types.IntType,
            "problem_created":types.IntType,
            "problem_translated":types.IntType,
            "problem_foundtypo":types.IntType,
            "problem_foundmistake_data":types.IntType,
            "problem_foundmistake_condition":types.IntType,
            "problem_adddata":types.IntType,
            "problem_found_noncecondition":types.IntType,
            "problem_foundwrongtranslation":types.IntType,
            "problem_createddata":types.IntType,
            "problem_createspecialjudge":types.IntType,
            "accepted":types.IntType,
            "wrong_output":types.IntType,
            "wrong":types.IntType,
            "tle":types.IntType,
            "mle":types.IntType,
            "output_exceed":types.IntType,
            "runtime":types.IntType,
            "compile":types.IntType,
            "school":types.StringType}
    def __init__(self, username='', description='', rank=0, solved=0, submitted=0, workbook_cleared=0, solution_written=0, contest_first=0, contest_second=0, problem_created=0, problem_translated=0, problem_foundtypo=0, problem_foundmistake_data=0, problem_foundmistake_condition=0, problem_adddata=0, problem_found_noncecondition=0, problem_foundwrongtranslation=0, problem_createddata=0, problem_createspecialjudge=0, accepted=0, wrong_output=0, wrong=0, tle=0, mle=0,
            output_exceed=0, runtime=0, compile=0, school=0):
        self.username = username
        self.description = description
        self.rank = rank
        self.solved = solved
        self.submitted = submitted
        self.workbook_cleared = workbook_cleared
        self.solution_written = solution_written
        self.contest_first = contest_first
        self.contest_second = contest_second
        self.problem_created = problem_created
        self.problem_translated = problem_translated
        self.problem_foundtypo = problem_foundtypo
        self.problem_foundmistake_data = problem_foundmistake_data
        self.problem_foundmistake_condition = problem_foundmistake_condition
        self.problem_adddata = problem_adddata
        self.problem_found_noncecondition = problem_found_noncecondition
        self.problem_foundwrongtranslation = problem_foundwrongtranslation
        self.problem_createddata = problem_createddata
        self.problem_createspecialjudge = problem_createspecialjudge
        self.accepted = accepted
        self.wrong_output = wrong_output
        self.wrong = wrong
        self.tle = tle
        self.mle = mle
        self.output_exceed = output_exceed
        self.runtime = runtime
        self.compile = compile
        self.school = school

        self._id_attrs = (self.username, )
class Status(BOJObject):
    __slots__ = ['idx', 'username', 'problem', 'result', 'memory', 'time', 'language', 'length', 'submit_time']
    __types__ = {
            "idx":types.IntType,
            "username":types.StringType,
            "problem":types.IntType,
            "result":types.IntType,
            "memory":types.IntType,
            "time":types.IntType,
            "language":types.StringType,
            "length":types.IntType,
            "submit_time":types.IntType
            }
    def __init__(self, idx=0, username='', problem=0, result=0, memory=0, time=0, language=0, length=0, submit_time=0):
        self.idx = idx
        self.username = username
        self.problem = problem
        self.result = result
        self.memory = memory
        self.time = time
        self.language = language
        self.length = length
        self.submit_time = submit_time

class Exercise(BOJObject):
    __slots__ = ['idx', 'title', 'first', 'second', 'start', 'end']
    __types__ = {
            "idx":types.IntType,
            "title":types.StringType,
            "first":types.StringType,
            "second":types.StringType,
            "start":types.IntType,
            "end":types.IntType
            }
    def __init__(self, idx=0, title='', first='', second='', start=0, end=0):
        self.idx = idx
        self.title = title
        self.first = first
        self.second = second
        self.start = start
        self.end = end
