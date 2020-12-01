import flywheel
import logging

log=logging.getLogger(__name__)
log.setLevel("DEBUG")

fw = flywheel.Client()




class level_export_template:
    def __init__(self, rc_record_field, fw_record_val, mappings, level):
        self.rc_record_field = rc_record_field
        self.fw_record_val = fw_record_val
        self.mappings = mappings
        self.level = level
        self.mapped_values = {}
        self.all_container_maps = {'maps': {}, 'files': {}}
        
        
    def generate_mappings(self, container):
        for map in self.mappings.maps:
            fw_key = list(map.keys())[0]
            rc_field = list(map.values())[0]
            val = expand_metadata(fw_key, container)
            self.mapped_values[rc_field] = val
    
    
    def create_rc_call(self):
        packet = {self.rc_record_field: self.fw_record_val}
        for rc_field, fw_value in self.mapped_values.items():
            packet[rc_field] = fw_value
        print('packet')
        print(packet)
        return(packet)
    
    
class export_map:
    def __init__(self, maps={}, files={}):
        self.maps = maps
        self.files = files


