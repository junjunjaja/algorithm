import numpy as np
import random
import requests
from collections import defaultdict,OrderedDict
x_auth_token = '2bf74c0a92acab37c46fa4373dca861d'


class User_Agent(object):
    def __init__(self,id,grade,minute):
        self.id = id
        self.grade = 40000
        self.minute = minute
        self.user_info = {}
        self.win_lose = [0,0]

    def game_time_func(self,grade2,r = True):
        if r:
            e = random.randint(-5, 5)
        else:
            e = 0
        t = 40 - (float(self.grade-grade2) / 99000.0)* 35 + e
        t = max(t,3)
        t = min(t,40)
        return t

    def r_game_time_func(self,time,r = True):
        if r:
            e = random.randint(-5, 5)
        else:
            e = 0
        grade2 = (self.grade) - (40-e-time)*99000 /35
        return grade2
    def winner_ratio(self,grade2):
        return (self.grade)/(self.grade+grade2),self.game_time_func(grade2)

class Abuser_User_Agent(User_Agent):
    def __init__(self,id,grade,minute):
        User_Agent.__init__(self,id=id,grade=grade,minute=minute)
        self.abuser = 0
        self.find_ab = False

    def abuser_winner_ratio(self,grade2):
        if grade2< self.grade:
            if random.randint(1,10) <=8:
                return 0.8,random.randint(3,10)
            else:
                return 0.2,random.randint(3,40)
        else:
            return self.winner_ratio(grade2),self.game_time_func(grade2)

class API_object(object):
    header = {'X-Auth-Token': x_auth_token,
              'Content-Type': 'application/json'}
    url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod/'
    def __init__(self,parent,proble):
        self.parent = parent
        self.proble = proble
        prob_key = self.get_request_key(proble)
        self.prob_header = {'Authorization': prob_key,
              'Content-Type': 'application/json'}

    def get_request_key(self,problem):
        param = {"problem": int(problem)}
        r = requests.post(self.url + 'start', headers=self.header, json=param)
        problem_auth_key = r.json()['auth_key']
        return problem_auth_key

    def waiting_line(self):
        """
        {
          "waiting_line": [
            { "id": 1, "from": 3 },
            { "id": 2, "from": 14 },
            ...
          ]
        }
        """
        r = requests.get(self.url + 'waiting_line', headers=self.prob_header)
        r = r.json()['waiting_line']
        for i in r:
            if i['id'] not in self.parent.waiting_dict:
                self.parent.waiting_dict[i['id']] = self.parent.user_dict[i['id']]
            self.parent.waiting_dict[i['id']].minute = self.parent.minute - i['from']


    def game_result(self):
        """
        {
          "game_result": [
            {"win": 10, "lose": 2, "taken": 7 },
            {"win": 7, "lose": 12, "taken": 33 },
            ...
          ]
        }
        """
        return requests.get(self.url + 'game_result', headers=self.prob_header).json()['game_result']

    def user_info(self):
        """
        {
          "user_info": [
            { "id": 1, "grade": 2100 },
            { "id": 13, "grade": 1501 },
            ...
          ]
        }
        """
        r = requests.get(self.url + 'user_info', headers=self.prob_header)
        r = r.json()['user_info']
        for i in r:
            if i['id'] not in self.parent.user_dict:
                if self.proble ==1:
                    self.parent.user_dict[i['id']] = User_Agent(i['id'],grade=40000,minute=9999)
                else:
                    self.parent.user_dict[i['id']] = Abuser_User_Agent(i['id'],grade=40000, minute=9999)
            else:
                self.parent.user_dict[i['id']].grade = i['grade']

    def match_api(self,data):
        """
        {
          "status": "ready",  #kakao game server status
          "time": 312  #from requst time +1 minute
        }
          "pairs": [[1, 2], [9, 7], [11, 49]]
        """
        data = {'pairs':data}
        r = requests.put(self.url + 'match', headers=self.prob_header,json=data)
        return r.json()

    def change_grade(self,commands):
        """
        "commands": [
         { "id": 1, "grade": 1900 }
         ...
       ]
        return : {
          "status": "ready"
        }
        """
        data = {'pairs':commands}
        r = requests.put(self.url + 'change_grade', headers=self.prob_header,json=data)
        return r.json()

    def score(self):
        """
        :return:
        {
          "status": "finished",
          "efficiency_score": 1.0,
          "accuracy_score1": 0.0,
          "accuracy_score2": 32.62,
          "score": 39.944
        }
        """
        r = requests.get(self.url + 'score', headers=self.prob_header)
        return r.json()


class Simulator(object):
    def __init__(self,simul='one',debug=False):
        self.user_dict = {}
        self.waiting_dict = OrderedDict()
        self.waiting_que = []
        self.debug = debug
        self.result = getattr(self,simul)()


    def one(self):
        TOTAL_USER = 30
        self.api = API_object(self,1)
        self.api.change_grade([{'id': i, 'grade': 40000} for i in range(1, TOTAL_USER + 1)])
        self.api.user_info()
        r = self.api.match_api([[]])
        self.minute = 1
        while (self.minute <= 600) or (r['status'] !='finished'):
            self.api.waiting_line()
            pairs = self.wait_user_make_pair()
            r = self.api.match_api(pairs)
            self.minute +=1
            game_ret = self.api.game_result()
            if len(game_ret):
                self.grade_update(game_ret)
            if self.debug:
                print(self.minute,len(game_ret))

        score = self.api.score()
        return score
    def two(self):
        TOTAL_USER = 900
        self.api = API_object(self, 2)
        self.api.change_grade([{'id': i, 'grade': 40000} for i in range(1, TOTAL_USER + 1)])
        self.api.game_result()
        self.api.user_info()
        r = self.api.match_api([[]])
        self.minute = 1
        while (self.minute <= 600) or (r['status'] != 'finished'):
            self.api.waiting_line()
            pairs = self.wait_user_make_pair()
            r = self.api.match_api(pairs)
            self.minute += 1
            game_ret = self.api.game_result()
            if len(game_ret):
                self.grade_update_abuser(game_ret)
            if self.debug:
                self.pprint2(game_ret)
        score = self.api.score()
        return score

    def pprint(self,game_ret):
        strs = f"""
        {self.minute} minute.
        {game_ret}
        {[(i,v.grade,v.win_lose) for i,v in self.user_dict.items()]}
        """
        print(strs)

    def pprint2(self,game_ret):
        strs = f"""
        {self.minute} minute.
        {game_ret}
        {[(i,v.grade,v.win_lose,v.abuser,v.find_ab) for i,v in self.user_dict.items() if v.abuser != 0]}
        """
        print(strs)


    def grade_update_abuser(self,game_ret):
        comm = []
        for game in game_ret:
            w = game['win']
            l = game['lose']
            t = game['taken']
            self.user_dict[w].win_lose[0] += 1
            self.user_dict[l].win_lose[1] += 1
            if t <= 10:
                self.user_dict[l].abuser += 1
                if self.user_dict[l].find_ab:
                    comm.append({'id': l, 'grade': int(self.user_dict[l].grade * 1.05)})
                    self.api.change_grade(l)
                    return
            else:
                w_ab = self.user_dict[w].abuser
                l_ab = self.user_dict[l].abuser
                if (w_ab >=5) and (l_ab) >=5:
                    self.user_dict[w].find_ab = True
                    self.user_dict[l].find_ab = True
            grade2 = self.user_dict[w].r_game_time_func(t, r=0)
            diff = self.user_dict[w].grade - grade2
            if t <= 10:
                diff /= 2
            for i in range(2,20):
                if diff//i <= (self.user_dict[l].grade-1000):
                    self.user_dict[w].grade += diff // i
                    self.user_dict[l].grade -= diff // i
                    break
            else:
                self.user_dict[w].grade += diff
            comm.append({'id':w,'grade':int(self.user_dict[w].grade)})
            comm.append({'id': l, 'grade': int(self.user_dict[l].grade)})
            self.api.change_grade(l)


    def grade_update(self,game_ret):
        comm = []
        for game in game_ret:
            w = game['win']
            l = game['lose']
            t = game['taken']
            self.user_dict[w].win_lose[0] += 1
            self.user_dict[l].win_lose[1] += 1
            grade2 = self.user_dict[w].r_game_time_func(t, r=0)
            diff = self.user_dict[w].grade - grade2
            for i in range(2,20):
                if diff//i <= (self.user_dict[l].grade-1000):
                    self.user_dict[w].grade += diff // i
                    self.user_dict[l].grade -= diff // i
                    break
            else:
                self.user_dict[w].grade += diff
            comm.append({'id':w,'grade':int(self.user_dict[w].grade)})
            comm.append({'id': l, 'grade': int(self.user_dict[l].grade)})
            self.api.change_grade(l)

    def wait_user_make_pair(self):
        ret = [i.id for i in sorted(self.waiting_dict.values(),key=lambda x: x.grade)]
        pairs = []
        while len(ret) > 1:
            i = ret.pop()
            j = ret.pop()
            pair = self.make_pairs(i,j)
            if pair is not None:
                del self.waiting_dict[i],self.waiting_dict[j]
                pairs.append(pair)
            else:
                ret.append(j)
        return pairs
    def make_pairs(self,i,j):
        g1 = self.user_dict[i].grade
        g2 = self.user_dict[j].grade
        if abs(g1-g2) > 1000:
            return None
        else:
            return [i,j]

if __name__ == "__main__":
    s1 = Simulator(simul='one',debug=False)
    print(s1.result)
    s2 = Simulator(simul='two',debug=False)
    print(s2.result)

