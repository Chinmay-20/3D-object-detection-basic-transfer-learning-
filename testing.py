import open3d.ml.torch as ml3d

dataset = ml3d.datasets.SemanticKITTI('./SemanticKitti/')

all_split = dataset.get_split('all')

print(all_split.get_attr(0))

print(all_split.get_data(0)['point'].shape)

vis = ml3d.vis.Visualizer()
vis.visualize_dataset(dataset, 'all', indices=range(340))
