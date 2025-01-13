
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')  # static 폴더 경로 설정

@app.route('/')
def home():
    # N명의 친구와 점수 및 전적
    players = {
        '박희열(2)': {'score': 1000, 'record': '0승 0패'},
        '박두병(3)': {'score': 1000, 'record': '0승 0패'},
        '박희석(3)': {'score': 1000, 'record': '0승 0패'},
        '정경태(4)': {'score': 1000, 'record': '0승 0패'},
        '최영중(4)': {'score': 1000, 'record': '0승 0패'},
        '송원횡(5)': {'score': 1000, 'record': '0승 0패'},
        '김원일(6)': {'score': 1000, 'record': '0승 0패'},
        '강동연(6)': {'score': 1000, 'record': '0승 0패'},
        '박해욱(6)': {'score': 1000, 'record': '0승 0패'},
        '박태종(6)': {'score': 1000, 'record': '0승 0패'},
        '승지관(6)': {'score': 1000, 'record': '0승 0패'},
        '최정우(6)': {'score': 1000, 'record': '0승 0패'},
        '황동훈(7)': {'score': 1000, 'record': '0승 0패'},
        '김명규(7)': {'score': 1000, 'record': '0승 0패'},
        '김휘수(7)': {'score': 1000, 'record': '0승 0패'},
        '박훈제(7)': {'score': 1000, 'record': '0승 0패'},
        '한상민(7)': {'score': 1000, 'record': '0승 0패'},
        '안용석(7)': {'score': 1000, 'record': '0승 0패'},
        '장재명(7)': {'score': 1000, 'record': '0승 0패'},
        '박영태(7)': {'score': 1000, 'record': '0승 0패'},
        '정행일(8)': {'score': 1000, 'record': '0승 0패'},
        '박수현(8)': {'score': 1000, 'record': '0승 0패'},
        '정재기(8)': {'score': 1000, 'record': '0승 0패'},
        '정환영(8)': {'score': 1000, 'record': '0승 0패'},
        '강태훈(8)': {'score': 1000, 'record': '0승 0패'},
        '정현대(8)': {'score': 1000, 'record': '0승 0패'},
        '박도용(8)': {'score': 1000, 'record': '0승 0패'},
        '김영찬(8)': {'score': 1000, 'record': '0승 0패'},
        '강호길(8)': {'score': 1000, 'record': '0승 0패'},
        '송재면(8)': {'score': 1000, 'record': '0승 0패'},
        '이찬우(8)': {'score': 1000, 'record': '0승 0패'},
        '임춘욱(8)': {'score': 1000, 'record': '0승 0패'},
        '임태민(8)': {'score': 1000, 'record': '0승 0패'},
        '장태현(8)': {'score': 1000, 'record': '0승 0패'},
        '하철암(8)': {'score': 1000, 'record': '0승 0패'},
        '한희정(8)': {'score': 1000, 'record': '0승 0패'},
        '권구용(8)': {'score': 1000, 'record': '0승 0패'},
        '윤병권(8)': {'score': 1000, 'record': '0승 0패'},
        '김지민(8)': {'score': 1000, 'record': '0승 0패'},
        '문기상(8)': {'score': 1000, 'record': '0승 0패'},
        '강상희(8)': {'score': 1000, 'record': '0승 0패'},
        '배공랄(5)': {'score': 1000, 'record': '0승 0패'},
        '김은혜(7)': {'score': 1000, 'record': '0승 0패'},
        '김혜자(7)': {'score': 1000, 'record': '0승 0패'},
        '김정희(7)': {'score': 1000, 'record': '0승 0패'},
        '신상희(7)': {'score': 1000, 'record': '0승 0패'},
        '김애신(9)': {'score': 1000, 'record': '0승 0패'},
        '손옥례(9)': {'score': 1000, 'record': '0승 0패'},
        '권명숙(9)': {'score': 1000, 'record': '0승 0패'},
        '이숙이(10)': {'score': 1000, 'record': '0승 0패'},
        '정경숙(10)': {'score': 1000, 'record': '0승 0패'},
        '강해린(10)': {'score': 1000, 'record': '0승 0패'},
        '강미정(10)': {'score': 1000, 'record': '0승 0패'},
        '공경옥(11)': {'score': 1000, 'record': '0승 0패'},
        '문명숙(11)': {'score': 1000, 'record': '0승 0패'},
        '한은영(11)': {'score': 1000, 'record': '0승 0패'},
        '한지연(11)': {'score': 1000, 'record': '0승 0패'},
        '하정희(11)': {'score': 1000, 'record': '0승 0패'},
        '강미정(11)': {'score': 1000, 'record': '0승 0패'},
        '진미라(11)': {'score': 1000, 'record': '0승 0패'},
        '황서영(11)': {'score': 1000, 'record': '0승 0패'},
    }
    
    # 점수를 기준으로 내림차순 정렬하여 등수 추가
    sorted_players = sorted(players.items(), key=lambda x: x[1]['score'], reverse=True)
    ranked_players = [
        {'rank': i + 1, 'name': name, 'score': data['score'], 'record': data['record']}
        for i, (name, data) in enumerate(sorted_players)
    ]

    # 결과를 템플릿으로 전달
    return render_template('index.html', ranked_players=ranked_players)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
