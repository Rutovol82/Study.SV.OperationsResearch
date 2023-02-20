import json
import attr
import paxb as pb


@pb.model(name='test')
class BoatInfo:
    name: str = pb.attribute(name='full_name')


obj = BoatInfo(name="Cum Girl")
obj4 = BoatInfo(name="Cum Girl")

string = pb.to_xml(obj, envelope="", ns='data', ns_map={'data': 'pysailing2'}, name='test2')
print(string)


print(hash(obj))
print(hash(obj4))
