import open3d as o3d

# Example Open3D geometry (use your own)
mesh = o3d.geometry.TriangleMesh.create_sphere()
o3d.io.write_triangle_mesh("/home/raniatze/Documents/PhD/Research/PrITTI/pritti_page/static/models/myscene.glb", mesh)
