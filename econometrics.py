
# coding: utf-8

# In[ ]:


def prop_diff_conf_int(counts, nobs, alpha=0.05):
    """
    Возвращает доверительный интервал для разности пропорций
    
    Параметры:
    ----------
    counts : список или массив количеств успехов в обеих выборках
    nobs : список или массив длин обеих выборок
    alpha : уровень значимости
    
    """
    
    if len(counts) != 2:
        raise ValueError('Неверная размерность параметра counts')
        
    if len(nobs) != 2:
        raise ValueError('Неверная размерность параметра nobs')
    
    if len(counts) == len(nobs) == 2:
        n1 = nobs[0]
        n2 = nobs[1]
        p1 = counts[0] / n1
        p2 = counts[1] / n2

        z = scipy.stats.norm.ppf(1 - alpha / 2)
        left_b = (p1 - p2) - z * np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
        right_b = (p1 - p2) + z * np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    
    return left_b, right_b


def prop_diff_z_stat(counts, nobs, ph=0):
    """
    Возвращает Z-статистику для теста на различие между
        двумя пропорциями в независимых выборках
    
    Параметры:
    ----------
    counts : список или массив количеств успехов в обеих выборках
    nobs : список или массив длин обеих выборок
    ph : разница между долями по нулевой гипотезе
    
    """
    
    if len(counts) != 2:
        raise ValueError('Неверная размерность параметра counts')
        
    if len(nobs) != 2:
        raise ValueError('Неверная размерность параметра nobs')
    
    if len(counts) == len(nobs) == 2:
        n1 = nobs[0]
        n2 = nobs[1]
        p1 = counts[0] / n1
        p2 = counts[1] / n2

        P = (p1 * n1 + p2 * n2) / (n1 + n2)
        std = np.sqrt(P * (1 - P) * (1 / n1 + 1 / n2))
        z = (p1 - p2 - ph) / std
    
    return z


def prop_diff_z_test(z_stat, alternative='two-sided'):
    """
    Возвращает p-value для Z-теста с заданными параметрами
    
    Параметры:
    ----------
    z_stat : вычисленное значение Z-статистики
    alternative : {'two-sided', 'less', 'greater'}
        симметричность теста
    
    """
    
    if alternative not in ('two-sided', 'less', 'greater'):
        raise ValueError('Неизвестное значение параметра alternative')
    
    if alternative == 'two-sided':
        p_value = 2 * (1 - scipy.stats.norm.cdf(np.abs(z_stat)))
        return p_value
    
    if alternative == 'less':
        p_value = scipy.stats.norm.cdf(z_stat)
        return p_value
    
    if alternative == 'greater':
        p_value = 1 - scipy.stats.norm.cdf(z_stat)
        return p_value

