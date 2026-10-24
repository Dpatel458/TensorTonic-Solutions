def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    x = x0
    for _ in range(steps):
        grad = 2*a*x + b #equation is given in the problem hence can directly give the derivative function
        x = x - lr * grad
        
    return float(x)
    pass