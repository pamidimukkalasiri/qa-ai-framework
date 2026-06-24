import time
import functools
from core.logger import logger

def retry(times: int=3, delay: float=0.1):
    """Retry a function if it raises an exception."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Attempt {attempt}/{times} failed"
                                   f"in {func.__name__}: {e}")
                    if attempt < times:
                        time.sleep(delay)
            raise Exception(f"{func.__name__} failed after {times} attempts")
        return wrapper
    return decorator

def log_action(func):
    """Log a function starts and completes"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"{func.__name__} started")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} completed")
        return result
    return wrapper

def timer(func):
    """Measure and log how long a function takes"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f"{func.__name__} took {elapsed:.2f} seconds")
        return result
    return wrapper