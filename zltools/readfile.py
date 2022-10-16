import os
import sys
import time
from threading import Thread

def animation(func_name='程序', *args, **kwargs):
    """ what's this

    Args:
        arg:
    Raises:
        error:

    """
    try:
        ani_str = '|/-\\'
        while(1):
            for i in range(len(ani_str)):
                print ( f'\r {func_name}正在运行： {ani_str[ i ]}', end='' )
                time.sleep(0.25)

    except Exception as e:
        print( f'  cause Error : {e}')

if __name__ == '__main__':


    ani = Thread(target=animation,)
    # time.sleep ( 5 )
    ani.start()
    ani.join(timeout=5)

    sys.exit()