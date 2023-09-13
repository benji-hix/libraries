
#* ------------- static method to calculate time since created_at ------------- #

#* SQL:
"""SELECT *, timestampdiff(hour, table.created_at, current_timestamp )
as hours_elapsed from table
"""

    # --------------------------- format hours elapsed --------------------------- #
    @staticmethod
    def format_time(list):
        for row in list:
            hours = row['time_elapsed']
            formatted_time = 0
            unit = ''
            if hours >= 8760:
                formatted_time =int(hours / 8760)
                if formatted_time == 1: unit = ' year'
                else: unit = ' years'
            elif hours >= 730:
                formatted_time = int(hours / 730)
                if formatted_time == 1: unit = ' month'
                else: unit = ' months'
            elif hours >= 168:
                formatted_time = int(hours / 168)
                if formatted_time == 1: unit = ' week'
                else: unit = ' weeks'
            elif hours >= 24:
                formatted_time = int(hours / 24)
                if formatted_time == 1: unit = ' day'
                else: unit = ' days'
            elif hours >= 1:
                formatted_time = hours
                if formatted_time == 1: unit = ' hour'
                else: unit = ' hours'
            else:
                row['time_elapsed'] = 'less than 1 hour'
            
            row['time_elapsed'] = str(formatted_time) + unit
        return list