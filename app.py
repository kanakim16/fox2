@app.route('/')
def home():
    # N명의 친구와 점수 및 전적
    players = [
        {'name': '은혜', 'score': 63, 'record': '5승 3패'},
        {'name': '원일', 'score': 30, 'record': '2승 6패'},
        {'name': '혜원', 'score': 100, 'record': '10승 0패'},
        {'name': '쌍두', 'score': 101, 'record': '8승 2패'},
        {'name': '금자', 'score': 300, 'record': '15승 1패'},
        {'name': '미선', 'score': 24, 'record': '1승 9패'},
        {'name': '익완', 'score': 111, 'record': '7승 3패'},
        {'name': '양두', 'score': 205, 'record': '12승 4패'},
        {'name': '만두', 'score': 165, 'record': '10승 5패'},
        {'name': '현지', 'score': 125, 'record': '9승 6패'},
    ]

    # 점수를 내림차순으로 정렬하여 등수 추가
    sorted_players = sorted(players, key=lambda x: x['score'], reverse=True)
    for rank, player in enumerate(sorted_players, 1):
        player['rank'] = rank

    # 결과를 템플릿으로 전달
    return render_template('index.html', players=sorted_players)
