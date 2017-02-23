from google.cloud import monitoring
import sys

def custom_metric(metric_descriptor):
    if 'custom.googleapis.com' in metric_descriptor.name:
        return True
    else:
        return False

def list_time_series(metric_descriptor):
    client = monitoring.Client()
    query_result = client.query(metric, minutes=5).iter(headers_only=True)
    for result in query_results:
        print(result)

def list_metric_descriptors():
    client = monitoring.Client()
    for descriptor in client.list_metric_descriptors():
        if custom_metric(descriptor):
            print descriptor.name

if  __name__ == '__main__':
    if len(sys.argv) == 1:
        list_metric_descriptors()
    else :
        list_time_series(sys.argv[1])
