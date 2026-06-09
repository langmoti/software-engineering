#############################################################################
# Fehlerbehandlung
# try:
#    # Run code that could go wrong
# except Exception as e: 
#    # Cleanup 
#    # raise -> Reraises the same or print warning etc.
# else:
#    # Run code if no error happened
# finally:
#    # Run code no mather if error happened or not
#
# except <Error> as e: | except <Error>:
# With 'as e' the error text can be accessed.
# Aside that, they are equal and several except can be written below one another.
# So different errors get caught at different excepts and can run different code. 
# Similar to elif in if else. 
#
# except Exception: universal valid for all errors.
# Exception is a class and subclasses are different exceptions like ValueError etc.
# So its similar working to inheritance of classes.
#
# Under except <error>: a raise can be set (without ()) and it will re-raise the same error.
# Idea behind it is, that required cleanup can be done before the error is passed to the caller.
# That can also catch it and then do its own cleanup. 
#
# Example for errors:
# ValueError, TypeError, FileNotFoundError and many many more.
# 
# To trigger an error on purpose:
# raise <Error>
# Example: raise FileNotFoundError -> triggers this error.
#
# raise TypeError('text') from e
# Raises this error as a result of the error e. 
# Can be added under an except ...: to make it part of the printed out error stack.
#
# Exceptions can also be created from scratch:
# class SelfMadeException(ValueError): -> can also inherit directly from Exception
#    pass -> Simply inherit everything
# Calling it:
# error = SelfMadeException('test')
# print(error) -> will show 'test' -> if more than one is given to error, will also print all as tuple
# print(error.args) -> will show ('test',) as tuple
# 
# Access error name: type(error).__name__
#############################################################################

#############################################################################
# Assertions:
# Code: assert x == 2, 'text'
# If assert is not True, the 'text' is printed out.
# Allows checking if function/variable works expected. 
# Usually to check and debugging in development code. 
# Not used in productive code. 
# python3 -O (O Buchstabe nicht Null) -> deaktiviert assertions beim Aufurf
#############################################################################
