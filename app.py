from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 3명의 친구와 점수
    scores = {
        '은혜': 63,
        '원일': 30,
        '혜원': 100,
        '쌍두': 101,
        '금자': 105,
    }

    # 점수를 내림차순으로 정렬하여 (이름, 점수) 튜플로 저장
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # 등수 추가: sorted_scores 리스트에 등수 정보를 추가
    ranked_scores = []
    for i, (name, score) in enumerate(sorted_scores, 1):
        ranked_scores.append((i, name, score))
    
    # 결과를 템플릿으로 전달
    return render_template('index.html', ranked_scores=ranked_scores)

if __name__ == '__main__':
    # 외부에서 접속할 수 있도록 host와 port 설정
    app.run(debug=True, host='0.0.0.0', port=5000)
