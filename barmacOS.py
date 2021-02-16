import rumps, webbrowser

class BarApp(rumps.App):
    @rumps.clicked('pythonexplainedto.me')
    def web(self, _):
        webbrowser.open('https://pythoneexplainedto.me', new=2)

if __name__ == "__main__" :
    BarApp("pythonexplainedto.me").run()