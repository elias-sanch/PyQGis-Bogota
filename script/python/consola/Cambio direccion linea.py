layer = QgsProject.instance().mapLayer('waterways20171005162048981')
id = 2679
r = QgsFeatureRequest(id)
features = layer.getFeatures(r)

feature = next(features)

geometry = feature.geometry()

lines = geometry.asMultiPolyline()
for line in lines:
    line.reverse()

new_geometry = QgsGeometry.fromMultiPolylineXY(lines)

with edit(layer):
    layer.changeGeometry(id, new_geometry)
    layer.triggerRepaint()