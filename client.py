from e_commerce.bigquery import BigQuery
from e_commerce.frame import profiler

df = BigQuery("./service-account.json").get_data("""
        SELECT
        channelGrouping AS traffic_type,
        device.deviceCategory AS device_type,
        date,
        fullVisitorId,
        IF
        ( COUNTIF ( totals.transactions > 0
            AND totals.newVisits IS NULL ) > 0,
            1,
            0 ) AS had_buy_on_return_visit,
        SUM(totals.visits) AS visits,
        SUM(totals.pageviews) AS pageviews,
        SUM(totals.bounces) AS bounces,
        SUM(totals.transactions) AS transactions,
        SUM(totals.transactionRevenue)/1000000 AS revenue,
        ROUND((SUM(totals.transactionRevenue)/1000000)/COUNT( fullVisitorId),2) AS revenue_per_user,
        ROUND(SUM(totals.pageviews)/COUNT( fullVisitorId),2) AS pageviews_per_user,
        ROUND(SUM(totals.transactions)/COUNT( fullVisitorId),2) AS transactions_per_user,
        FROM
        `bigquery-public-data.google_analytics_sample.ga_sessions_*`
        WHERE
        _TABLE_SUFFIX BETWEEN '20160801'
        AND '20160831'
        GROUP BY
        channelGrouping,
        device_type,
        date,
        fullVisitorId
""")


profiler(df)
