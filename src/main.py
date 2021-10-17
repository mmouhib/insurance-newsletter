from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# todo add loading animation and hide form while sending mails (add event listener on submit button)
