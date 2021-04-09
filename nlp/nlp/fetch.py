import twint


def tweets():
    c = twint.Config()
    c.Search = '"hashnode" OR @hashnode  OR #hashnode'
    c.Filter_retweets = True
    c.Since = "2020-06-24"
    c.Until = "2020-08-20"
    c.Store_csv = True
    c.Output = "data"
    twint.run.Search(c)