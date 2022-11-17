class DataStream:
    
    def __init__(self):
        self.data_stream_output = []
        self.data_string_list = []
    
    def should_output_data_str(self, timestamp: int, data_string: str):
        
        
        if timestamp in [timestamp, timestamp-5] and data_string in self.data_string_list:
            self.data_stream_output.append(False)
        else:
            self.data_stream_output.append(True)
            
        if len(self.data_string_list) == 0:
            self.data_string_list.append(data_string)
        else:
            self.data_string_list.pop()
            self.data_string_list.append(data_string)
        return self.data_stream_output
            
    