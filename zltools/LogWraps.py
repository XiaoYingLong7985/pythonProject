# 记录函数调用信息的装饰器
def setlog(func) :
    """ what's this

    Args:

    Raises:
        error:

    """
    # 将funcs的元信息复制给run函数
    from functools import wraps
    from datetime import datetime
    import time
    log_file = 'C:\PycharmProjects\pythonProject\logs\setlog.log'

    @wraps ( func )
    def run(*args, **kwargs) :
        with open ( log_file, 'a+' ) as f :
            f.write ( f'{func.__name__} run at: {datetime.fromtimestamp ( time.time () )} \r' )

        return func ( *args, **kwargs )

    return run