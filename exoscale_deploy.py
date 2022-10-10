from tracemalloc import Snapshot
import exoscale_deploy
exo = exoscale_deploy.Exoscale()

zone_gva2 = exo.compute.get_zone("ch-gva-2")
security_group_web = exo.compute.get_security_group("default")

# Create instance
instance_fed = exo.compute.create_instance(
     name="Cloudsys-Deploy-Front",
     zone=zone_gva2,
     type=exo.compute.get_instance_type("medium"),
     template=exo.compute.get_instance_template(
            zone_gva2, "32e8b0f0-8cc9-4f88-bb46-8b7b508ebd11"),
     volume_size=50,
     security_groups=[security_group_web],
    )  

print(f"Instance {instance_fed.name} created")
print(instance_fed.name, instance_fed.id, instance_fed.ipv4_address)

# Create instance 2
instance_bed = exo.compute.create_instance(
     name="Cloudsys-Deploy-Back",
     zone=zone_gva2,
     type=exo.compute.get_instance_type("medium"),
     template=exo.compute.get_instance_template(
            zone_gva2, "7704d409-158d-48cf-be22-4a161a028dd6"),
     volume_size=50,
     security_groups=[security_group_web],
    )  

print(f"Instance {instance_bed.name} created")
print(instance_bed.name, instance_bed.id, instance_bed.ipv4_address)

# Create bucket
bucket = exo.storage.create_bucket("cloudsys-deploy", zone="ch-gva-2")
print("Bucket created:", bucket.name)