def load_user(user_id):
    try:
        print(id_user)
    except Exception as e:
        e.add_note(f"user_id={user_id}")
        e.add_note("while loading profile data")
        raise e
try:
  load_user(1)
except Exception as e:
  print(e.note)
