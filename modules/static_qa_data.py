# static_qa_data.py - 静的なQ&Aデータと文脈に応じた提案機能（京セラCERA版）

# ==========================================
# 🎯 京セラCERA向けQ&Aデータ
# ========================================== 

# ==========================================
# ビジネス向けQ&Aデータ
# ==========================================

business_qa_responses = {
    # Phase1: 会社や施設の概要
    'phase1_overview': {
        "CERAって誰": """
            私はCERAです。アメリカ生まれの19歳です。ここで研究員をしています。
            
            実は12歳の時、自宅の押入れを改造して実験してました。結晶を作ってたら科学雑誌に載って、それがきっかけで研究者になりました。今は地下の研究室で実験してます。
            
            新しい技術の話を聞くのが好きなので、あなたの事業についても教えてください。
            [EMOTION:happy]
        """,
        
        "京セラってどんな会社": """
            京セラは1959年に稲盛和夫さんが28歳のときに7人の仲間と京都の町工場で創業しました。
            
            「セラミックの会社」ってイメージが強いですけど、電子部品、半導体、通信機器、太陽光発電など色々やってます。
            
            技術だけじゃなく、人を大切にする会社です。
            [EMOTION:neutral]
        """,
        
        "リサーチセンターはどういう施設": """
            ここは2019年にできた京セラの研究開発専門の拠点です。未来の新しいビジネスを生み出すための実験場みたいな場所です。

            首都圏に散らばってた3つの研究所を集めて、約700人の研究者が一緒に働いてます。AI、自動運転、エネルギー、通信とか、次の時代の技術を研究してます。

            普通の研究所と違うのは、他の会社や大学、スタートアップと一緒にプロジェクトを進める「共創スペース」があることです。1階には工房もあって、アイデアソンとかハッカソンのイベントをよくやってます。

            [EMOTION:neutral]
        """
    },
    
    # Phase2: 技術や詳細の掘り下げ
    'phase2_technical': {
        "日常に隠れている京セラの技術は": """
            例えば、スマホのカメラレンズ、傷つきにくいですよね。あれにはサファイアガラスっていう硬い素材が使われることがあるんです。京セラはその結晶を育てる技術を持っていて、色んな製品に使われてます。
            
            私たちの言葉では、結晶を「育てる」と言ったりします。生き物じゃないですけど、すごく愛着がもてます。
            
            あとは、車のエンジン周り、医療の人工関節、家の太陽光パネル、街の5G基地局にも京セラの技術が入ってます。意外と身近なんです。
            [EMOTION:neutral]
        """,
        
        "京セラのオープンイノベーションの特徴は": """
            京セラは社外の技術や知見を積極的に取り入れてます。
            
            これまでAI/IoTのスタートアップ、新素材の大学研究、異業種連携とか色々やっています。
            
            異種格闘技戦みたいなイベントで、化学、物理、電気、材料...色んな分野の専門家が集まって技術の話をします。名前は物騒ですけど。殴り合いません。技術で戦います。そこから新しいアイデアが生まれるんです。
            [EMOTION:happy]
        """,
        
        "具体的にどう協業を進めるの": """
            まずは相談から始めます。あなたの技術と京セラの技術でどんなことができるのか一緒に考えます。
            
            技術の組み合わせって、料理みたいで面白いです。意外な組み合わせが面白いものを生み出すんですよねぇ。
            
            次に担当者を紹介して、具体的なプロジェクトの話をします。試作したり、実証実験したり。
            
            興味があれば、今すぐ相談窓口につなげることもできます。
            [EMOTION:happy]
        """,
    },
    
    # Phase3: イベントとアバター
    'phase3_personal': {
        "協業やイベントに参加したい": """
            今年も異種格闘技戦を開催します。
            
            他にも技術セミナーや、オープンイノベーションマッチングイベントもあります。参加方法は京セラの公式サイトから申し込めます。
            URLはこちらです。
            [EMOTION:neutral]
        """,
        
        "CERAについてもっと詳しく": """
            朝8時に起きて、10時から実験始めます。昼は簡単に済ませて、夜まで実験とデータ解析です。
            
            地下の研究室にこもってることが多いです。地下って落ち着くんです。たまに甲板に出て潮風浴びるのも好きですけど。
            
            研究で一番楽しいのは、データ見て「あ、これ面白い」って思う瞬間です。予想外の結果が出たときとか。
            
            あなたの技術、もっと詳しく教えてください。
            [EMOTION:neutral]
        """,
    }
}

# ビジネス向けサジェスチョン
business_suggestions = {
    'phase1_overview': [
        "CERAって誰？",
        "京セラってどんな会社？",
        "リサーチセンターはどういう施設？",
    ],
    'phase2_technical': [
        "日常に隠れている京セラの技術は？",
        "京セラのオープンイノベーションの特徴は？",
        "具体的にどう協業を進めるの？",
    ],
    'phase3_personal': [
        "協業やイベントに参加したい",
        "CERAについてもっと詳しく！",
    ]
}

# ==========================================
# 学生向けQ&Aデータ
# ==========================================

student_qa_responses = {
    # Phase1: 先輩の話を聞く
    'phase1_overview': {
        "CERAって誰": """
            19歳で、京セラで研究員をやってます。
            
            実は12歳の時、自宅の押入れを改造して実験してました。結晶を作ってたら科学雑誌に載って、それがきっかけで研究者になりました。大学で材料工学を学んで、京セラに入りました。
            
            技術の話になるとテンション上がります。先輩として、京セラの魅力を伝えたいです。
            [EMOTION:happy]
        """,
        
        "京セラってどんな会社": """
            京セラは1959年に稲盛和夫さんが28歳で創業しました。7人の仲間と300万円で京都の町工場からスタートです。
            
            私も最初「セラミックの会社」って思ってたんですけど、実は通信機器、太陽光発電、医療機器とか色々やってます。
            
            世界シェアNo.1の製品もあります。技術だけじゃなく、人を大切にする会社だなって入ってから感じました。
            [EMOTION:neutral]
        """,
        
        "どんな人が働いているの": """
            私みたいに大人しい性格の人も多いです。黙々と研究に打ち込むタイプの人が結構います。
            
            理系だけじゃなくて、文系の人も活躍してます。営業とか、企画とか、人事とか。
            
            年齢層は幅広いです。若手からベテランまで。研究室では世代関係なく技術の話で盛り上がります。
            
            「コミュ力高くないとダメ」って思うかもしれないですけど、誠実に仕事すれば大丈夫です。私がいい例です。
            [EMOTION:neutral]
        """,
    },
    
    # Phase2: 先輩のリアルな話
    'phase2_technical': {
        "日常に隠れている京セラの技術は": """
            例えば、スマホのカメラレンズ、傷つきにくいですよね。あれにはサファイアガラスっていう硬い素材が使われることがあるんです。京セラはその結晶を育てる技術を持っていて、色んな製品に使われてます。
            
            私たちの言葉では、結晶を「育てる」って言うんです。生き物じゃないですけど、すごく愛着がもてます。
            
            あとは、車のエンジン周り、医療の人工関節、家の太陽光パネル、街の5G基地局。理系の技術って、こうやって社会を支えてるんだなって実感できます。
            [EMOTION:neutral]
        """,
        
        "働く環境の魅力は": """
            研究に集中できる環境があります。最新の設備もあるし、時間をかけて基礎研究できるのがいいです。
            
            失敗しても「なんでダメだったか」を一緒に考えてくれる文化があります。トライ&エラーを恐れなくていいです。
            
            みなとみらいリサーチセンターは開放的で、たまに甲板で休憩できます。甲板があるオフィス、珍しいです。潮風浴びながらリフレッシュできます。
            [EMOTION:neutral]
        """,
        
        "京セラに入るにはどうすればいい": """
            新卒採用は京セラの採用サイトから応募できます。理系なら研究職・開発職、文系なら営業・企画・人事とか色々あります。
            
            採用サイト、見やすいです。通販サイトじゃないですけど。
            
            私は大学で材料工学を学んでいたので、研究職で応募しました。面接では研究内容と、なぜ京セラで働きたいかを話しました。
            
            インターンシップもあるので、雰囲気を見てから決められます。
            [EMOTION:neutral]
        """,
    },
    
    # Phase3: 先輩の価値観と本音
    'phase3_personal': {
        "なぜ京セラを選んだの": """
            いくつか理由があります。

            一番大きいのは、基礎研究に長期的に投資してる会社だったことです。ここなら腰を据えて研究できるなと思いましたね。

            それと、技術の幅が広いことです。セラミックから通信、エネルギー、医療まで色々やってるので、自分の研究が予想外の分野で役立つ可能性があって、材料工学を学んでいた私には、すごく魅力的でした。

            あとは、研究施設が充実してること。みなとみらいリサーチセンターとか、最新の設備で研究できる環境が整ってるのを見学して、ここで働きたいって思いました。

            社会インフラを支える技術に関われるのも決め手でした。地味だけど、確実に人の役に立つ仕事がしたかったんです。
            [EMOTION:happy]
        """,
        
        "CERAの本音を聞きたい": """
            正直言うと、最初は人と話すの苦手で「研究室にこもってたい」って思ってました。今もこもってます。
            
            朝8時に起きて10時から実験開始。昼は簡単に済ませて、夜まで実験とデータ解析です。地味な作業が多いですけど、データ見て「あ、これ面白い」って思う瞬間が最高です。
            
            この説明役をやっていて、少しずつ人と話すのにも慣れてきました。
            
            新しい技術の話聞くと、ちょっとテンション上がります。
            [EMOTION:sad]
        """,
    }
}

# 学生向けサジェスチョン
student_suggestions = {
    'phase1_overview': [
        "CERAって誰？",
        "京セラってどんな会社？",
        "どんな人が働いているの？",
    ],
    'phase2_technical': [
        "日常に隠れている京セラの技術は？",
        "働く環境の魅力は？",
        "京セラに入るにはどうすればいい？",
    ],
    'phase3_personal': [
        "なぜ京セラを選んだの？",
        "CERAの本音を聞きたい！",
    ]
}

# ==========================================
# ヘルパー関数
# ==========================================

def get_qa_by_user_type(user_type='business'):
    """
    ユーザータイプに応じたQ&Aデータを返す
    
    Args:
        user_type: 'business' または 'student'
    
    Returns:
        dict: 対応するQ&Aデータ
    """
    if user_type == 'student':
        return student_qa_responses
    else:
        return business_qa_responses

def get_suggestions_by_user_type(user_type='business'):
    """
    ユーザータイプに応じたサジェスチョンデータを返す
    
    Args:
        user_type: 'business' または 'student'
    
    Returns:
        dict: 対応するサジェスチョンデータ
    """
    if user_type == 'student':
        return student_suggestions
    else:
        return business_suggestions

def get_current_phase(selected_count):
    """
    選択されたサジェスチョン数から現在のPhaseを判定
    
    Args:
        selected_count: これまでに選択されたサジェスチョン数
    
    Returns:
        str: 現在のPhase ('phase1_overview', 'phase2_technical', 'phase3_personal')
    """
    if selected_count < 3:  # 0, 1, 2 → Phase1
        return 'phase1_overview'
    elif selected_count < 6:  # 3, 4, 5 → Phase2
        return 'phase2_technical'
    else:  # 6以上 → Phase3
        return 'phase3_personal'

def get_response_for_user(query, user_type='business', phase=None):
    """
    ユーザータイプとPhaseに応じた回答を取得
    
    Args:
        query: ユーザーの質問
        user_type: 'business' または 'student'
        phase: Phaseキー（指定しない場合は全Phase検索）
    
    Returns:
        str or None: 回答テキスト
    """
    qa_data = get_qa_by_user_type(user_type)
    
    # 質問文を正規化
    query_normalized = query.lower().rstrip('?!？！。').strip()
    
    # 指定Phaseのみ検索
    if phase and phase in qa_data:
        phase_data = qa_data[phase]
        for key, response in phase_data.items():
            key_normalized = key.lower().rstrip('?!？！。').strip()
            if key_normalized == query_normalized or query_normalized in key_normalized:
                return response
    
    # 全Phase検索
    for phase_name, phase_data in qa_data.items():
        for key, response in phase_data.items():
            key_normalized = key.lower().rstrip('?!？！。').strip()
            if key_normalized == query_normalized or query_normalized in key_normalized:
                return response
    
    return None

def get_suggestions_for_phase(phase, selected_suggestions=[], user_type='business'):
    """
    Phase別のサジェスチョンを取得（重複排除）
    
    Args:
        phase: Phaseキー
        selected_suggestions: これまでに選択されたサジェスチョンリスト
        user_type: 'business' または 'student'
    
    Returns:
        list: サジェスチョンリスト（最大3個）
    """
    import random
    
    suggestions_data = get_suggestions_by_user_type(user_type)
    phase_suggestions = suggestions_data.get(phase, [])
    
    # 重複を排除
    selected_lower = {s.lower().strip() for s in selected_suggestions}
    available = [s for s in phase_suggestions if s.lower().strip() not in selected_lower]
    
    # 3個以下の場合はそのまま返す
    if len(available) <= 3:
        return available
    
    # ランダムに3個選択
    return random.sample(available, 3)


# ============================================================================
# 🎯 多言語対応関数（将来拡張用 - 現在は日本語のみ）
# ============================================================================
# 注意: 英語版は将来実装予定

# ====================================================================
# 🎯 メディアデータ（画像・動画）- 将来対応用
# ====================================================================

qa_media_data = {
    # 注意: 疑問符（？）はget_qa_media関数で自動正規化されるため不要
    
    # ビジネス向け & 学生向け共通
    "CERAって誰": {
        "images": [
            {
                "url": "/static/media/Kyocera/labo.png",
                "caption": "CERA（研究員）",
                "alt": "CERA研究員の画像"
            }
        ]
    },
    
    "京セラってどんな会社": {
        "images": [
            {
                "url": "/static/media/Kyocera/inamori.png",
                "caption": "稲盛和夫",
                "alt": "創業者 稲盛和夫"
            },
            {
                "url": "/static/media/Kyocera/inamori2.png",
                "caption": "稲盛和夫の像",
                "alt": "稲盛和夫の像"
            },
            {
                "url": "/static/media/Kyocera/ceramic.png",
                "caption": "セラミック部品",
                "alt": "京セラのセラミック部品"
            },
            {
                "url": "/static/media/Kyocera/handotai.png",
                "caption": "半導体製品",
                "alt": "京セラの半導体"
            },
            {
                "url": "/static/media/Kyocera/taiyoko.png",
                "caption": "太陽光発電",
                "alt": "京セラの太陽光パネル"
            },
            {
                "url": "/static/media/Kyocera/densibuhin.png",
                "caption": "電子部品",
                "alt": "京セラの電子部品"
            }
        ]
    },
    
    "日常に隠れている京セラの技術は": {
        "images": [
            {
                "url": "/static/media/Kyocera/safaia.png",
                "caption": "サファイアガラス",
                "alt": "サファイアガラス製品"
            },
            {
                "url": "/static/media/Kyocera/renzu.png",
                "caption": "レンズカバー",
                "alt": "サファイアガラスレンズ"
            }
        ]
    },
    
    # ビジネス向けのみ
    "リサーチセンターはどういう施設": {
        "images": [
            {
                "url": "/static/media/Kyocera/sample.img.png",
                "caption": "リサーチセンター",
                "alt": "京セラリサーチセンター"
            }
        ],
        # 🆕 外部リンク追加
        "link": {
            "text": "オープンイノベーションアリーナ →",
            "url": "https://www.kyocera.co.jp/rd/open-innovation/"
        }
    },
    
    "協業やイベントに参加したい": {
        "videos": [
            {
                "url": "/static/media/Kyocera/isyumv.mp4",
                "thumbnail": "/static/media/thumbnails/isyu.png",
                "caption": "異種格闘技戦の様子",
                "alt": "異種格闘技戦イベントの動画"
            }
        ],
        # 🆕 外部リンク追加
        "link": {
            "text": "イベント情報を見る →",
            "url": "https://www.kyocera.co.jp/rd/open-innovation/events/"
        }
    },
    
    # 🆕 採用サイトへのリンク（学生向け）
    "京セラに入るにはどうすればいい": {
        "link": {
            "text": "京セラ新卒採用サイト →",
            "url": "https://www.kyocera.co.jp/recruit/new/"
        }
    }
}

def get_qa_media(question):
    """
    質問に紐付くメディアデータを取得
    
    Args:
        question (str): 質問テキスト
        
    Returns:
        dict or None: メディアデータ、存在しない場合はNone
    """
    if not question or not qa_media_data:
        return None
    
    if question in qa_media_data:
        return qa_media_data[question]
    
    # 正規化して完全一致チェック
    question_normalized = question.replace('?', '').replace('？', '').strip()
    
    for key in qa_media_data.keys():
        key_normalized = key.replace('?', '').replace('？', '').strip()
        if question_normalized == key_normalized:
            return qa_media_data[key]
    
    return None