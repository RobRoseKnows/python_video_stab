from setuptools import setup

setup(name='vidstab',
      version=version['__version__'],
      description='Video Stabilization using OpenCV',
      author='Adam Spannbauer',
      author_email='RobRoseKnows+Git@gmail.com',
      url='https://github.com/RobRoseKnows/python_video_stab',
      packages=['vidstab'],
      license='MIT',
      install_requires=[
          'numpy',
          'imutils'
      ],
      extras_require={
        'cv2':  ['opencv-contrib-python >= 3.4.0']
      },
      test_suite='nose.collector',
      tests_require=['nose'],
      keywords=['video stabilization', 'computer vision', 'image processing', 'opencv']
      )
