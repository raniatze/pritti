import open3d as o3d

# Example Open3D geometry (use your own)
# mesh = o3d.geometry.TriangleMesh.create_sphere()
# o3d.io.write_triangle_mesh("/home/raniatze/Documents/PhD/Research/PrITTI/pritti_page/static/models/myscene.glb", mesh)

# Create a cuboid (box)
mesh = o3d.geometry.TriangleMesh.create_box(width=1.0, height=2.0, depth=3.0)
mesh.compute_vertex_normals()

# Save it to a GLB file (note: this may not be supported depending on your Open3D version)
o3d.io.write_triangle_mesh("cuboid.glb", mesh)

