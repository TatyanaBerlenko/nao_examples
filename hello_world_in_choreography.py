class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        # put initialization code here
        print('onLoad')
        pass

    def onUnload(self):
        print('onUnload!')
        pass

    def onInput_onStart(self):
        # self.onStopped() #activate the output of the box
        print('onStart!')

    def onInput_onStop(self):
        print('onStopped!')
        self.onUnload()  # it is recommended to reuse the clean-up as the box is stopped
        self.onStopped()  # activate the output of the box