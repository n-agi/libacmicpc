#coding: utf-8
from Model import *
import requests
from BeautifulSoup import BeautifulSoup as bs
class LoginError(Exception):
    pass
class NoUserFoundException(Exception):
    pass
class Parser:
    def __init__(self, username="", password=""):
        self.s = requests.session()
        self.logined = False
        self.username = username
        self.password = password
        while not self.login():
            continue
    def login(self):
        if self.username == "" or self.password == "":
            return
        if self.logined:
            return
        payload = {"login_user_id":self.username,
                "login_password":self.password,
                "next":"/"
                }
        req = self.s.post("https://www.acmicpc.net/signin", payload)
        b = bs(req.text)
        r = (b.find("meta", attrs={"name":"username"})['content'] == self.username)
        self.logined = r
        return r
    #idx, name, description
    def getGroup(self, idx=543):
        if not self.logined:
            raise LoginError()
        url = "https://www.acmicpc.net/group/%d" % (idx)
        req = self.s.get(url)
        b = bs(req.text)
        ph = b.find("div", attrs={"class":"page-header"})
        group_name = ph.find("h1").text
        group_description = ph.find("blockquote").text
        return Group(idx, group_name, group_description)
    # g must be the instance of class Group
    def getGroupUsers(self, g=None):
        if not self.logined:
            raise LoginError()
        if not isinstance(g, Group):
            raise TypeError("getGroupUsers must call with class Group")
        url = "https://www.acmicpc.net/group/member/%d" % (g.idx)
        req = self.s.get(url)
        b = bs(req.text)
        members = b.findAll("div", attrs={"class":"col-xs-6 col-sm-4 col-md-3 member"})
        return map(lambda x: x.find("a").text, members)
    def getStatus(self, start=-1):
        def toTimestamp(s):
                return int(datetime.datetime.strptime(s, '%Y년 %m월 %d일 %H시 %M분 %S초').strftime("%s") )
        def resultToInt(s):
            table = {u"맞았습니다!!":4,u"출력 형식이 잘못되었습니다":5, u"틀렸습니다":6, u"시간 초과":7, u"메모리 초과":8, u"출력 초과":9, u"런타임 에러":10, u"기다리는 중":0, u"재채점을 기다리는 중":1, u"컴파일 하는 중":2, u"채점중":3}
            try:
                return table[s]
            except:
                return 0
        if not self.logined:
            raise LoginError()
        url = 'https://www.acmicpc.net/status/?group_id=543'
        if start >= 0:
            url += '&top=%d' % (start)
        req = self.s.get(url)
        b = bs(req.text)
        tbody = b.find("tbody")
        ret = []
        for tr in tbody.findAll("tr"):
            tds = tr.findAll("td")
            idx = int(tds[0].text)
            username = tds[1].text
            problem = int(tds[2].text)
            result = resultToInt(tds[3].text)
            try:
                memory = int(tds[4].text.split(" ")[0])
            except:
                memory = 0
            try:
                time = int(tds[5].text.split(" ")[0])
            except:
                time = 0
            language = tds[6].text
            length = int(tds[7].text.split(" ")[0])
            submitTime = int(tds[8].find("a")['data-timestamp'])
            ret.append(Status(idx, username, problem, result, memory, time, language, length, submitTime))
        return ret
    def getUser(self, username=''):
        #self, username='', description='', rank=0, solved=0, submitted=0, workbook_cleared=0, solution_written=0, contest_first=0, contest_second=0, problem_created=0, problem_translated=0, problem_foundtypo=0, problem_foundmistake_data=0,                      problem_foundmistake_condition=0, problem_adddata=0, problem_found_noncecondition=0, problem_foundwrongtranslation=0, problem_createddata=0, problem_createspecialjudge=0, accepted=0, wrong_output=0, wrong=0, tle=0, mle=0,
        #runtime=0, compile=0, school=0
        url = "https://www.acmicpc.net/user/%s" % (username)
        req = self.s.get(url)
        if req.status_code == 404:
            raise NoUserFoundException("User {0} not found.".format(username))
        b = bs(req.text)
        ph = b.find("div", attrs={"class":"page-header"})
        username = ph.find("h1").text
        description = ph.find("blockquote").text
        stats = b.find("table", attrs={"id":"statics"})
        u = User(username, description)
        for tr in stats.findAll("tr"):
            th = tr.find("th").text
            td = tr.find("td").text
            if th == u'랭킹':
                u.rank = int(td)
            elif th == u'푼 문제':
                u.solved = int(td)
            elif th == u'제출':
                u.submitted = int(td)
            elif th == u'문제집 클리어':
                u.workbook_cleared = int(td)
            elif th == u'문제 풀이':
                u.solution_written = int(td)
            elif th == u'대회 우승':
                u.contest_first = int(td)
            elif th == u'대회 준우승':
                u.contest_second = int(td)
            elif th == u'만든 문제':
                u.problem_created = int(td)
            elif th == u'번역한 문제':
                u.problem_translated = int(td)
            elif th == u'오타를 찾음':
                u.problem_foundtypo = int(td)
            elif th == u'잘못된 데이터를 찾음':
                u.problem_foundmistake_data = int(td)
            elif th == u'잘못된 조건을 찾음':
                u.problem_foundmistake_condition = int(td)
            elif th == u'데이터를 추가':
                u.problem_adddata = int(td)
            elif th == u'빠진 조건을 찾음':
                u.problem_found_noncecondition = int(td)
            elif th == u'잘못된 번역을 찾음':
                u.problem_foundwrongtranslation = int(td)
            elif th == u'데이터를 추가':
                u.problem_createddata = int(td)
            elif th == u'스페셜 저지를 만듦':
                u.problem_createspecialjudge = int(td)
            elif th == u'맞았습니다':
                u.accepted = int(td)
            elif th == u'출력 형식':
                u.wrong_output = int(td)
            elif th == u'틀렸습니다':
                u.wrong = int(td)
            elif th == u'시간 초과':
                u.tle = int(td)
            elif th == u'메모리 초과':
                u.mle = int(td)
            elif th == u'출력 초과':
                u.output_exceed = int(td)
            elif th == u'런타임 에러':
                u.runtime = int(td)
            elif th == u'컴파일 에러':
                u.compile = int(td)
        return u
