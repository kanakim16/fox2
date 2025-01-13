
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')  # static 폴더 경로 설정

@app.route('/')
def home():
    # N명의 친구와 점수 및 전적
    players = {
        '김원일(6)': {'score': 1000, 'record': '0승 0패'},
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
