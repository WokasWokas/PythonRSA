if __name__ == "__main__":
    try:
        from Form.main import create_form

        form = create_form()
        
        form.start()

    except Exception as error:
        print(error)
        print("Exception ({}) raised from {} with message (\n  {}\n)".format(error.__class__.__name__, error.__traceback__.tb_frame.f_code.co_filename, error.args[0]))