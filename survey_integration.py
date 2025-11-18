# survey_integration.py
# Googleスプレッドシート連携アンケートシステム（最終確定版）

import os
from datetime import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class SurveyManager:
    """アンケート管理クラス (Googleスプレッドシート連携)"""
    
    def __init__(self, credentials_path='credentials.json', spreadsheet_id=None):
        """
        初期化
        
        Args:
            credentials_path: サービスアカウントのJSONファイルパス
            spreadsheet_id: スプレッドシートのID
        """
        self.credentials_path = credentials_path
        self.spreadsheet_id = spreadsheet_id or os.getenv('SPREADSHEET_ID')
        self.service = None
        self.enabled = False
        
        # 初期化を試行
        self._initialize()
    
    def _initialize(self):
        """Google Sheets APIサービスを初期化"""
        try:
            # 認証情報ファイルの存在確認
            if not os.path.exists(self.credentials_path):
                print(f"⚠️ 認証情報ファイルが見つかりません: {self.credentials_path}")
                print("💡 アンケート機能は無効化されます")
                return
            
            # スプレッドシートIDの確認
            if not self.spreadsheet_id:
                print("⚠️ SPREADSHEET_IDが設定されていません")
                print("💡 アンケート機能は無効化されます")
                return
            
            # 認証情報を読み込み
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            creds = Credentials.from_service_account_file(
                self.credentials_path, 
                scopes=SCOPES
            )
            
            # APIサービスを構築
            self.service = build('sheets', 'v4', credentials=creds)
            self.enabled = True
            
            print(f"✅ Google Sheets API初期化成功")
            print(f"📊 スプレッドシートID: {self.spreadsheet_id[:20]}...")
            
        except Exception as e:
            print(f"❌ Google Sheets API初期化エラー: {e}")
            print("💡 アンケート機能は無効化されます")
            self.enabled = False
    
    def save_survey(self, survey_data):
        """
        アンケート結果をスプレッドシートに保存
        
        Args:
            survey_data: アンケートデータの辞書
                {
                    'visitor_id': 訪問者ID,
                    'quiz_score': クイズスコア (0-3),
                    'conversation_count': 会話回数,
                    'q1': Q1属性,
                    'q2': Q2関心度 (1-5),
                    'q3': Q3興味項目（カンマ区切り）,
                    'language': 言語 ('ja' or 'en')
                }
        
        Returns:
            bool: 保存成功ならTrue、失敗ならFalse
        """
        if not self.enabled:
            print("⚠️ アンケート機能が無効です")
            return False
        
        try:
            # タイムスタンプを生成
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # スプレッドシートに追加する行データ
            values = [[
                timestamp,
                survey_data.get('visitor_id', 'unknown'),
                survey_data.get('quiz_score', 0),
                survey_data.get('conversation_count', 0),
                survey_data.get('q1', ''),
                survey_data.get('q2', ''),
                survey_data.get('q3', ''),
                survey_data.get('language', 'ja')
            ]]
            
            body = {'values': values}
            
            # スプレッドシートに追加
            result = self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range='シート1!A:H',  # A列からH列まで（8列）
                valueInputOption='RAW',
                insertDataOption='INSERT_ROWS',
                body=body
            ).execute()
            
            print(f"✅ アンケート保存成功: {result.get('updates').get('updatedRows')}行追加")
            print(f"📝 データ: 属性={survey_data.get('q1')}, 関心度={survey_data.get('q2')}, 興味={survey_data.get('q3')}")
            return True
            
        except HttpError as e:
            print(f"❌ Google Sheets APIエラー: {e}")
            return False
        except Exception as e:
            print(f"❌ アンケート保存エラー: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def get_survey_stats(self):
        """
        アンケート統計を取得
        
        Returns:
            dict: 統計情報
        """
        if not self.enabled:
            return {'enabled': False}
        
        try:
            # スプレッドシートからデータを取得
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range='シート1!A:H'
            ).execute()
            
            values = result.get('values', [])
            
            if len(values) <= 1:  # ヘッダーのみ
                return {
                    'enabled': True,
                    'total_responses': 0,
                    'average_interest': 0
                }
            
            # 統計計算 (ヘッダー行を除く)
            data_rows = values[1:]
            total = len(data_rows)
            
            # Q2（関心度）の平均を計算
            interest_scores = [int(row[5]) for row in data_rows if len(row) > 5 and row[5].isdigit()]
            avg_interest = sum(interest_scores) / len(interest_scores) if interest_scores else 0
            
            return {
                'enabled': True,
                'total_responses': total,
                'average_interest': round(avg_interest, 2)
            }
            
        except Exception as e:
            print(f"❌ 統計取得エラー: {e}")
            return {'enabled': True, 'error': str(e)}


# ====== アンケート質問定義（最終確定版） ======
SURVEY_QUESTIONS = {
    'ja': [
        {
            'id': 'q1',
            'type': 'radio',
            'question': 'あなたの属性を教えてください',
            'options': [
                {'value': 'highschool', 'label': '~高校生'},
                {'value': 'university', 'label': '大学生・大学院生'},
                {'value': 'startup', 'label': 'スタートアップ・ベンチャー'},
                {'value': 'company', 'label': '一般企業'},
                {'value': 'research', 'label': '大学・研究機関'},
                {'value': 'government', 'label': '行政・自治体'},
                {'value': 'other', 'label': 'その他'}
            ]
        },
        {
            'id': 'q2',
            'type': 'rating',
            'question': 'CERAとの会話を通して、京セラへの興味・関心は深まりましたか？',
            'options': [
                {'value': '5', 'label': '5 - 大きく深まった'},
                {'value': '4', 'label': '4 - やや深まった'},
                {'value': '3', 'label': '3 - 変わらない'},
                {'value': '2', 'label': '2 - やや薄れた'},
                {'value': '1', 'label': '1 - 薄れた'}
            ]
        },
        {
            'id': 'q3',
            'type': 'checkbox',
            'question': '以下のうち、興味を持ったものを選んでください（複数選択可）',
            'options': [
                {'value': 'event', 'label': '京セラのイベント・異業種交流会への参加'},
                {'value': 'collaboration', 'label': '京セラとの協創・連携'},
                {'value': 'recruitment', 'label': '京セラの採用情報'},
                {'value': 'technology', 'label': '京セラの技術・製品についてもっと知りたい'},
                {'value': 'none', 'label': '特になし'}
            ]
        }
    ],
    'en': [
        {
            'id': 'q1',
            'type': 'radio',
            'question': 'Please select your affiliation',
            'options': [
                {'value': 'highschool', 'label': 'High school student or younger'},
                {'value': 'university', 'label': 'University/Graduate student'},
                {'value': 'startup', 'label': 'Startup/Venture'},
                {'value': 'company', 'label': 'General company'},
                {'value': 'research', 'label': 'University/Research institution'},
                {'value': 'government', 'label': 'Government/Local government'},
                {'value': 'other', 'label': 'Other'}
            ]
        },
        {
            'id': 'q2',
            'type': 'rating',
            'question': 'Has your interest in Kyocera deepened through conversation with CERA?',
            'options': [
                {'value': '5', 'label': '5 - Significantly deepened'},
                {'value': '4', 'label': '4 - Somewhat deepened'},
                {'value': '3', 'label': '3 - No change'},
                {'value': '2', 'label': '2 - Slightly decreased'},
                {'value': '1', 'label': '1 - Decreased'}
            ]
        },
        {
            'id': 'q3',
            'type': 'checkbox',
            'question': 'What are you interested in? (Multiple choices allowed)',
            'options': [
                {'value': 'event', 'label': 'Kyocera events/cross-industry meetings'},
                {'value': 'collaboration', 'label': 'Co-creation/collaboration with Kyocera'},
                {'value': 'recruitment', 'label': 'Kyocera recruitment information'},
                {'value': 'technology', 'label': 'Learn more about Kyocera technology/products'},
                {'value': 'none', 'label': 'None in particular'}
            ]
        }
    ]
}