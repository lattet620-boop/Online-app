from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from jnius import autoclass

# Android ရဲ့ Webview Library ကို လှမ်းခေါ်ခြင်း
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity

class WebViewWidget(BoxLayout):
    def init(self, **kwargs):
        super(WebViewWidget, self).init(**kwargs)
        self.webview = WebView(Activity)
        self.webview.getSettings().setJavaScriptEnabled(True) # JavaScript ခွင့်ပြုရန်
        self.webview.setWebViewClient(WebViewClient())
        
        # ဆရာ့ရဲ့ GitHub Public Link ကို ဒီနေရာမှာ ထည့်ပေးပါ
        self.webview.loadUrl('https://lattet620-boop.github.io/Online-app/') 
        
        Activity.setContentView(self.webview)

class MainApp(App):
    def build(self):
        return WebViewWidget()

if name == 'main':
    MainApp().run()
