            {
            
            '625': lambda data: [
                ('GLVBMS current', int(self.get_byte(data,0) + self.get_byte(data,1), 16)/1000)
            ],
            
            }
