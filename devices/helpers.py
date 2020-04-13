import time
import pandas as pd

from django.core.files.storage import default_storage


# timestamp = 946684800 + epoch embedded Y2K
# epoch embedded Y2K: 01/01/2000
# epoch Unix: 01/01/1970
MINUTE_IN_SECOND = 60
HOUR_IN_SECOND = MINUTE_IN_SECOND * 60 # 3,600
DAY_IN_SECOND = HOUR_IN_SECOND * 24  # 86,400
WEEK_IN_SECOND = DAY_IN_SECOND * 7 # 604,800

def get_previous(time_, unix_seconds):

    if time_ == 'minute':
        second_ = unix_seconds % 60
    if time_ == 'hour':
        second_ = unix_seconds % 3600
    elif time_ == 'day':
        second_ = unix_seconds % 86400
    else:
        second_ = unix_seconds % 60

    return unix_seconds - second_

def get_next(time_, unix_seconds):

    if time_ == 'minute':
        second = unix_seconds % 60
        second_ = 60 - second
    if time_ == 'hour':
        second = unix_seconds % 3600
        second_ = 3600 - second
    elif time_ == 'day':
        second = unix_seconds % 86400
        second_ = 86400 - second
    else:
        second = unix_seconds % 60
        second_ = 60 - second

    return unix_seconds + second_



def process_data(device_id, frequency, start_date, end_date):

    device_id_string = device_id.hex    

    start_date_file = get_previous('minute', start_date)
    end_date_file = get_next('minute', end_date) + 60

    csv_list = []

    for filename_second in range(start_date_file, end_date_file, 60):
        try:
            filename = 'devices/' + device_id_string + '/raw/' + str(filename_second) + '.csv'
            csv_file = default_storage.open(filename, 'r')
            df = pd.read_csv(csv_file, index_col=None, header=0)
            csv_list.append(df)
        except OSError:
            return 'OSError'
        except ValueError:
            return 'ValueError'
        

    frame = pd.concat(li, axis=0, ignore_index=True)
    
    if frequency == 'minute':
        pass
    elif frequency == 'hour':
        pass
    elif frequency == 'day':
        pass
    else:
        pass


    return '123'




def device_reading(device_id, frequency, end_date):
    
    end_date = int(time.time())

    if frequency == 'minute':
        # Get minute data in the last hour
        start_date = end_date - HOUR_IN_SECOND
    elif frequency == 'hour':
        # Get hour data in the last day
        start_date = end_date - DAY_IN_SECOND
    elif frequency == 'day':
        # Get day data in the last week
        start_date = end_date - WEEK_IN_SECOND
    else:
        # Default is second...
        start_date = end_date - MINUTE_IN_SECOND        
        
    reading_list = process_data(device_id, frequency, start_date, end_date)

    json_message = {
        'id': device_id.hex,
        'frequency': frequency,
        'start_date': start_date,
        'end_date': end_date,
        'readings': reading_list
    }

    return json_message

    """
    if sensor == 'current':
        pass
    elif sensor == 'voltage':
        pass
    elif sensor == 'energy':
        pass
    elif sensor == 'realPower':
        pass
    elif sensor == 'apparentPower':
        pass
    elif sensor == 'reactivePower':
        pass        
    elif sensor == 'hz':
        pass        
    else:
        pass
    """
    """
    if frequency == 'second':
        pass
    """