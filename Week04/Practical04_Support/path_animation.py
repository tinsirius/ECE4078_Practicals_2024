import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import numpy as np
import math

import meshcat
import meshcat.geometry as g
import meshcat.transformations as tf
from meshcat.animation import Animation
import time

def draw_polygon_obstacles(vis, name, polygon, thickness, robot_size): 
    points = polygon.compute_inner_vertices(thickness/2 + robot_size)
    for i in range(points.shape[0]):
        start = points[i][:]
        end = points[(i+1) % points.shape[0]][:]
        v = end - start
        length = np.linalg.norm(v)
        unit_v = (v / length)
        midpoint = (start + end) / 2
        vis[name]["poly" + str(i)].set_object(g.Box([length, thickness, 0]), 
            g.MeshLambertMaterial(color=0x000000,reflectivity=0))

        vis[name]["poly" + str(i)].set_transform(
            tf.translation_matrix([midpoint[0], midpoint[1], 0]) @ 
            tf.rotation_matrix(np.arccos(unit_v[0]) if unit_v[1] > 0 else
                               - np.arccos(unit_v[0]), [0,0,1]))
        vis[name]["corner" + str(i)].set_object(g.Sphere(thickness/2),
            g.MeshLambertMaterial(color=0x000000,reflectivity=0))
        vis[name]["corner" + str(i)].set_transform(
            tf.translation_matrix([start[0], start[1], 0]))

def animate_path_bug(vis,initial_robot_pos,goal_pos,path,obstacles,robot_size,wall_thickness, goal_line = True):
    # Set plot variables
    for i, obstacle in enumerate(obstacles):
        draw_polygon_obstacles(vis, "wall" + str(i), obstacle, wall_thickness, robot_size)
    
    if goal_line:
        vis["birdline"].set_object(
            g.Line(g.PointsGeometry(np.array([initial_robot_pos, goal_pos]).transpose()), 
            g.LineBasicMaterial(color=0xff0000, opacity=0.3)))
    else:
        vis["start"].set_object(g.Sphere(0.5), g.MeshLambertMaterial(color = 0x00ff00))
        vis["start"].set_transform(tf.translation_matrix([initial_robot_pos[0],initial_robot_pos[1],0]))
        vis["end"].set_object(g.Sphere(0.5), g.MeshLambertMaterial(color = 0x0000ff))
        vis["end"].set_transform(tf.translation_matrix([goal_pos[0],goal_pos[1],0]))
    
    vis["bot"].set_object(g.Sphere(robot_size), g.MeshLambertMaterial(color=0x00ff00))
    vis["bot"].set_transform(tf.translation_matrix([initial_robot_pos[0], initial_robot_pos[1], 0]))
    
    anim = Animation()
    
    for i in range(len(path)):
        trail = np.zeros((3, i))
        trail[:2, :] = np.array(path[:i, :]).transpose()
        vis["trail"].set_object(
            g.Line(g.PointsGeometry(trail), 
            g.LineBasicMaterial(color=0x00ff00)))
        vis["bot"].set_transform(tf.translation_matrix([path[i][0], path[i][1], 0]))
        anim.at_frame(vis, i)["bot"].set_transform(
            tf.translation_matrix([path[i][0], path[i][1], 0]))
        
        time.sleep(1/120.0)

    vis.set_animation(anim, play=False)

def plot_stick(start, end):
    v = end - start
    length = np.linalg.norm(v)
    unit_v = (v / length)
    midpoint = (start + end) / 2
    angle = np.arccos(unit_v[0]) if unit_v[1] > 0 else - np.arccos(unit_v[0])
    
    return length, midpoint, angle

def animate_path_rrt(vis, rrt):
    path = rrt.planning()
    for i, obs in enumerate(rrt.obstacle_list):
        cx, cy = obs.center
        r = obs.radius
        vis["obs"]["cicle" + str(i)].set_object(
            g.Cylinder(0,r), 
            g.MeshLambertMaterial(color = 0xff0000))
        vis["obs"]["cicle" + str(i)].set_transform(
            tf.translation_matrix([cx,cy,0]) @
            tf.rotation_matrix(np.pi/2, [1,0,0]))
    
    vis["start"].set_object(g.Sphere(0.1), g.MeshLambertMaterial(color = 0x00ff00))
    vis["start"].set_transform(tf.translation_matrix([rrt.start.x,rrt.start.y,0]))
    vis["end"].set_object(g.Sphere(0.1), g.MeshLambertMaterial(color = 0x0000ff))
    vis["end"].set_transform(tf.translation_matrix([rrt.end.x,rrt.end.y,0]))
    
    for i, node in enumerate(rrt.node_list):
        if node.parent:
            for j in range(len(node.path_x)):
                vis["node"]["p" + str(i) + str(j)].set_object(
                    g.Sphere(0.05),
                    g.MeshLambertMaterial(color = 0x00ff00))
                vis["node"]["p" + str(i) + str(j)].set_transform(
                    tf.translation_matrix([node.path_x[j], node.path_y[j], 0]))
            for j in range(len(node.path_x) - 1):
                start = np.array([node.path_x[j], node.path_y[j]])
                end = np.array([node.path_x[(j + 1)], node.path_y[j + 1]])
                length, midpoint, angle = plot_stick(start, end)
                vis["node"]["s" + str(i) + str(j)].set_object(g.Box([length, 0.02, 0]), 
                    g.MeshLambertMaterial(color=0x000000,reflectivity=0))
                vis["node"]["s" + str(i) + str(j)].set_transform(
                    tf.translation_matrix([midpoint[0], midpoint[1], 0]) @ 
                    tf.rotation_matrix(angle, [0,0,1])) 
    if path is not None:
        path_in_order = np.flipud(path)
        num_segments = len(path_in_order) - 1
        for i in range(num_segments):
            length, midpoint, angle = plot_stick(path_in_order[i, :], path_in_order[i + 1, :])
            vis["path"]["p" + str(i)].set_object(g.Box([length, 0.07, 0]), 
                    g.MeshLambertMaterial(color=0x0000ff,reflectivity=0))
            vis["path"]["p" + str(i)].set_transform(
                    tf.translation_matrix([midpoint[0], midpoint[1], 0]) @ 
                    tf.rotation_matrix(angle, [0,0,1]))
        anim = Animation()
        for i in range(num_segments + 1):
            for j in range(num_segments):
                anim.at_frame(vis, i*3)["path"]["p" + str(j)].set_property(
                    'visible', "boolean", False)
            for j in range(i):
                anim.at_frame(vis, i*3)["path"]["p" + str(j)].set_property(
                    'visible', "boolean", True)
        vis.set_animation(anim, play=False)
    else:
        print("Path was not found!!")

def animate_path_rrtc(vis, rrtc):
    path = rrtc.planning()
    for i, obs in enumerate(rrtc.obstacle_list):
        cx, cy = obs.center
        r = obs.radius
        vis["obs"]["cicle" + str(i)].set_object(
            g.Cylinder(0,r), 
            g.MeshLambertMaterial(color = 0xff0000))
        vis["obs"]["cicle" + str(i)].set_transform(
            tf.translation_matrix([cx,cy,0]) @
            tf.rotation_matrix(np.pi/2, [1,0,0]))
    
    vis["start"].set_object(g.Sphere(0.1), g.MeshLambertMaterial(color = 0x00ff00))
    vis["start"].set_transform(tf.translation_matrix([rrtc.start.x,rrtc.start.y,0]))
    vis["end"].set_object(g.Sphere(0.1), g.MeshLambertMaterial(color = 0x0000ff))
    vis["end"].set_transform(tf.translation_matrix([rrtc.end.x,rrtc.end.y,0]))
    
    for i, node in enumerate(rrtc.start_node_list):
        if node.parent:
            for j in range(len(node.path_x)):
                vis["node"]["ps" + str(i) + str(j)].set_object(
                    g.Sphere(0.05),
                    g.MeshLambertMaterial(color = 0x00ff00))
                vis["node"]["ps" + str(i) + str(j)].set_transform(
                    tf.translation_matrix([node.path_x[j], node.path_y[j], 0]))
            for j in range(len(node.path_x) - 1):
                start = np.array([node.path_x[j], node.path_y[j]])
                end = np.array([node.path_x[(j + 1)], node.path_y[j + 1]])
                length, midpoint, angle = plot_stick(start, end)
                vis["node"]["ss" + str(i) + str(j)].set_object(g.Box([length, 0.04, 0]), 
                    g.MeshLambertMaterial(color=0x00ff00,reflectivity=0))
                vis["node"]["ss" + str(i) + str(j)].set_transform(
                    tf.translation_matrix([midpoint[0], midpoint[1], 0]) @ 
                    tf.rotation_matrix(angle, [0,0,1]))
    for i, node in enumerate(rrtc.end_node_list):
        if node.parent:
            for j in range(len(node.path_x)):
                vis["node"]["pe" + str(i) + str(j)].set_object(
                    g.Sphere(0.05),
                    g.MeshLambertMaterial(color = 0x0000ff))
                vis["node"]["pe" + str(i) + str(j)].set_transform(
                    tf.translation_matrix([node.path_x[j], node.path_y[j], 0]))
            for j in range(len(node.path_x) - 1):
                start = np.array([node.path_x[j], node.path_y[j]])
                end = np.array([node.path_x[(j + 1)], node.path_y[j + 1]])
                length, midpoint, angle = plot_stick(start, end)
                vis["node"]["se" + str(i) + str(j)].set_object(g.Box([length, 0.04, 0]), 
                    g.MeshLambertMaterial(color=0x0000ff,reflectivity=0))
                vis["node"]["se" + str(i) + str(j)].set_transform(
                    tf.translation_matrix([midpoint[0], midpoint[1], 0]) @ 
                    tf.rotation_matrix(angle, [0,0,1])) 
                
    if path is not None:
        path_in_order = np.flipud(path)
        num_segments = len(path_in_order) - 1
        for i in range(num_segments):
            length, midpoint, angle = plot_stick(path_in_order[i, :], path_in_order[i + 1, :])
            vis["path"]["p" + str(i)].set_object(g.Box([length, 0.07, 0]), 
                    g.MeshLambertMaterial(color=0xff0000,reflectivity=0))
            vis["path"]["p" + str(i)].set_transform(
                    tf.translation_matrix([midpoint[0], midpoint[1], 0]) @ 
                    tf.rotation_matrix(angle, [0,0,1]))
        anim = Animation()
        for i in range(num_segments + 1):
            for j in range(num_segments):
                anim.at_frame(vis, i*3)["path"]["p" + str(j)].set_property(
                    'visible', "boolean", False)
            for j in range(i):
                anim.at_frame(vis, i*3)["path"]["p" + str(j)].set_property(
                    'visible', "boolean", True)
        vis.set_animation(anim, play=False)
    else:
        print("Path was not found!!")


def animate_path_prm(vis, rmap, start, goal, path, path_thickness = 0.5):
    obs = rmap.obstacles.data
    num_obs = len(obs)
    for i, ob in enumerate(obs):
        vis["wall"]["p" + str(i)].set_object(g.Sphere(0.5), 
                                            g.MeshLambertMaterial(color = 0x000000))
        vis["wall"]["p" + str(i)].set_transform(
            tf.translation_matrix([ob[0], ob[1], 0]))
    
    for i, v_edges in enumerate(rmap.edges):
        for j, e_idx in enumerate(v_edges):
            v_from = rmap.vertices[i,:]
            v_to = rmap.vertices[e_idx,:]
            vis["road"]["r" + str(i) + str(j)].set_object(
                g.Line(g.PointsGeometry(np.array([v_from, v_to]).transpose())))
    
    vis["start"].set_object(g.Sphere(0.5), g.MeshLambertMaterial(color = 0xff0000))
    vis["start"].set_transform(tf.translation_matrix([start[0],start[1],0]))
    vis["end"].set_object(g.Sphere(0.5), g.MeshLambertMaterial(color = 0x00ff00))
    vis["end"].set_transform(tf.translation_matrix([goal[0],goal[1],0]))
    
    if path is not None:
        path_in_order = np.flipud(path)
        num_segments = len(path_in_order) - 1
        for i in range(num_segments):
            length, midpoint, angle = plot_stick(path_in_order[i, :], path_in_order[i + 1, :])
            vis["path"]["p" + str(i)].set_object(g.Box([length, path_thickness, 0]), 
                    g.MeshLambertMaterial(color=0x01bfff,reflectivity=0))
            vis["path"]["p" + str(i)].set_transform(
                    tf.translation_matrix([midpoint[0], midpoint[1], 0]) @ 
                    tf.rotation_matrix(angle, [0,0,1]))
        anim = Animation()
        for i in range(num_segments + 1):
            for j in range(num_segments):
                anim.at_frame(vis, i*3)["path"]["p" + str(j)].set_property(
                    'visible', "boolean", False)
            for j in range(i):
                anim.at_frame(vis, i*3)["path"]["p" + str(j)].set_property(
                    'visible', "boolean", True)
        vis.set_animation(anim, play=False)
    else:
        pass
