from gui import App
from controllers import PageController, Pages

def main():
   app = App()
   PageController.set_page(app, Pages.PROFILE)
   app.mainloop()


if __name__ == '__main__':
    main()
