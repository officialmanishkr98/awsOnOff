import os  
import yaml   # parsing yaml file for default config values
import onOff

# Load the YAML file
with open('default_config.yaml', 'r') as yaml_file:
    config = yaml.safe_load(yaml_file)

def main():
    try:
        service = 'ec2'
        action = 'stop'
        region = 'us-west-2'

        if service not in ["ec2", "rds", "ecs"]:
            raise ValueError(f"Unknown service: {service}")

        if service == "ec2" and action == 'start':
            print(f"Orders are for EC2 service.")
            onOff.start_all_ec2( region ) 
        
        if service == "ec2" and action == 'stop':
            print(f"Orders are for EC2 service.")
            onOff.stop_all_ec2( region ) 


    # try:
    #     service = os.getenv('service')
    #     if service not in ["ec2", "rds", "ecs"]:
    #         raise ValueError(f"Unknown service: {service}")

    #     if service == "ec2":
    #         print(f"Orders are for EC2 service.")
    #         import ec2
    #         ec2.manage_ec2_instance(region, action) 

    #     elif service == "rds":
    #         print(f"Orders are for RDS service.")
    #         import rds
    #         rds.manage_rds_clusters(region, action)

    #     elif service == "ecs":
    #         print(f"Orders are for ECS service.")
    #         import ecs
    #         ecs.manage_ecs_clusters(region, action) 
                
    except Exception as err:
        print(f"There has been an error that says ==> {err}")


if __name__ == '__main__':
    main()