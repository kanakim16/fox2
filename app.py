
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')  # static 폴더 경로 설정

@app.route('/')
def home():
    # N명의 친구와 점수 및 전적
    players = {
        '은혜': {'score': 301, 'record': '5승 3패'},
        '원일': {'score': 30, 'record': '2승 8패'},
        '혜원': {'score': 100, 'record': '9승 1패'},
        '쌍두': {'score': 101, 'record': '8승 2패'},
        '금자': {'score': 300, 'record': '15승 5패'},
        '미선': {'score': 24, 'record': '1승 9패'},
        '익완': {'score': 111, 'record': '10승 5패'},
        '양두': {'score': 205, 'record': '12승 3패'},
        '만두': {'score': 165, 'record': '11승 4패'},
        '현지': {'score': 125, 'record': '7승 7패'},
        '은혜2': {'score': 302, 'record': '7승 7패'},
        '은혜3': {'score': 304, 'record': '7승 7패'},
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
