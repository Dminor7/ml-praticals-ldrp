from pandas_profiling import ProfileReport

def profiler(df,minimal=True):
    profile = ProfileReport(df, title="Pandas Profiling Report",minimal=minimal)
    return profile