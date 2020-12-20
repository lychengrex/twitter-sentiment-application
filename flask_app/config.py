from multiprocessing import cpu_count


def max_workers():
    return cpu_count()


bind = "0.0.0.0:8000"
workers = max_workers()
threads = 2

loglevel = "info"
errorlog = "logs/error.log"
accesslog = "logs/access.log"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'