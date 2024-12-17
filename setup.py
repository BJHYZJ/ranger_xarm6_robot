from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ranger_xarm6_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    # data_files=[
    #     ('share/ament_index/resource_index/packages',
    #         ['resource/' + package_name]),
    #     ('share/' + package_name, ['package.xml']),
    #     (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    #     (os.path.join('share', package_name, 'urdf/C1480'), glob('urdf/C1480/**')),
    #     (os.path.join('share', package_name, 'urdf/ranger_mini_v3'), glob('urdf/ranger_mini_v3/**')),
    #     (os.path.join('share', package_name, 'world'), glob('world/**')),
    # ],

    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'world'), glob('world/*')),

        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.*')),  
        (os.path.join('share', package_name, 'urdf/ranger_mini_v3'), glob('urdf/ranger_mini_v3/*.*')),
        (os.path.join('share', package_name, 'urdf/xarm_6'), glob('urdf/xarm_6/*.*')),
        (os.path.join('share', package_name, 'urdf/xarm_gripper'), glob('urdf/xarm_gripper/*.*')),

        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.*')),
        (os.path.join('share', package_name, 'meshes/box'), glob('meshes/box/*.*')),
        (os.path.join('share', package_name, 'meshes/ranger_mini_v3'), glob('meshes/ranger_mini_v3/*.*')),
        (os.path.join('share', package_name, 'meshes/xarm_6'), glob('meshes/xarm_6/*.*')),
        (os.path.join('share', package_name, 'meshes/xarm_gripper'), glob('meshes/xarm_gripper/*.*')),        
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yanzj',
    maintainer_email='yanzhijie@buaa.edu.cn',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
