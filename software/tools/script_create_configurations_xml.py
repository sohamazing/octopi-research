from lxml import etree as ET
top = ET.Element('modes')

mode_1 = ET.SubElement(top,'mode')
# ID = ET.SubElement(mode_1,'ID')
# ID.text = '123'
mode_1.set('ID','1')
mode_1.set('Name','BF LED matrix full')
mode_1.set('ExposureTime','100')
mode_1.set('AnalogGain','10')
mode_1.set('IlluminationSource','0')
mode_1.set('IlluminationIntensity','100')
mode_1.set('CameraSN','')
mode_1.set('ZOffset','0.0')

mode_2 = ET.SubElement(top,'mode')
mode_2.set('ID','2')
mode_2.set('Name','BF LED matrix left half')
mode_2.set('ExposureTime','100')
mode_2.set('AnalogGain','10')
mode_2.set('IlluminationSource','1')
mode_2.set('IlluminationIntensity','100')
mode_2.set('CameraSN','')
mode_2.set('ZOffset','0.0')

mode_3 = ET.SubElement(top,'mode')
mode_3.set('ID','3')
mode_3.set('Name','BF LED matrix right half')
mode_3.set('ExposureTime','100')
mode_3.set('AnalogGain','10')
mode_3.set('IlluminationSource','2')
mode_3.set('IlluminationIntensity','100')
mode_3.set('CameraSN','')
mode_3.set('ZOffset','0.0')

mode_4 = ET.SubElement(top,'mode')
mode_4.set('ID','4')
mode_4.set('Name','BF LED matrix color PDAF')
mode_4.set('ExposureTime','100')
mode_4.set('AnalogGain','10')
mode_4.set('IlluminationSource','3')
mode_4.set('IlluminationIntensity','100')
mode_4.set('CameraSN','')
mode_4.set('ZOffset','0.0')

mode_5 = ET.SubElement(top,'mode')
mode_5.set('ID','5')
mode_5.set('Name','Fluorescence 405 nm Ex')
mode_5.set('ExposureTime','100')
mode_5.set('AnalogGain','10')
mode_5.set('IlluminationSource','11')
mode_5.set('IlluminationIntensity','100')
mode_5.set('CameraSN','')
mode_5.set('ZOffset','0.0')

mode_6 = ET.SubElement(top,'mode')
mode_6.set('ID','6')
mode_6.set('Name','Fluorescence 488 nm Ex')
mode_6.set('ExposureTime','100')
mode_6.set('AnalogGain','10')
mode_6.set('IlluminationSource','12')
mode_6.set('IlluminationIntensity','100')
mode_6.set('CameraSN','')
mode_6.set('ZOffset','0.0')

mode_7 = ET.SubElement(top,'mode')
mode_7.set('ID','7')
mode_7.set('Name','Fluorescence 638 nm Ex')
mode_7.set('ExposureTime','100')
mode_7.set('AnalogGain','10')
mode_7.set('IlluminationSource','13')
mode_7.set('IlluminationIntensity','100')
mode_7.set('CameraSN','')
mode_7.set('ZOffset','0.0')

# print(ET.tostring(top, encoding="UTF-8", pretty_print=True).decode())
tree = ET.ElementTree(top)
tree.write('configurations.xml',encoding="utf-8", xml_declaration=True, pretty_print=True)
