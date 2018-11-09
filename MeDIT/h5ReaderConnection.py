import numpy as np
import h5py
import os
import sys
from copy import deepcopy
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from MeDIT.h5Reader import *
# from MeDIT.SaveAndLoad import LoadH5Info, LoadH5


class h5ReaderConnection(QMainWindow, Ui_h5Reader):
    def __init__(self, parent=None):
        super(h5ReaderConnection, self).__init__(parent)
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.LoadH5File)

    def LoadH5File(self):
        dlg = QFileDialog()
        data_path, _ = dlg.getOpenFileName(self, 'Choose a H5 file', filter="h5 file (*.h5)")
        if data_path:
            # print('data_path', data_path)
            self.label.setText("FilePath:" + data_path)
            data_h5 = h5py.File(data_path, 'r')
            self.tree.clear()
            self.root = QTreeWidgetItem(self.tree)
            self.root.setText(0, 'root')
            self.ProcessInit(self.root, data_h5)
            data_h5.close()

    def ProcessInit(self, node, data_h5_obj):
        # hdf5 file is also a Group object,so call ProcessGroup function
        self.ProcessGroup(node, data_h5_obj)
        QMessageBox.about(self, "OK", "load finished")
        # bind item click
        self.tree.itemDoubleClicked.connect(self.onTreeClicked)

    def onTreeClicked(self):
        current_data = self.tree.currentItem().data(0, 1)
        if current_data is not None:
            if current_data.shape.__len__() == 1:
                self.ProcessArray1D(current_data)
            elif current_data.shape.__len__() == 2:
                self.ProcessArray2D(current_data)
            else:
                self.ProcessArray3D(current_data)

    def ProcessGroup(self, node, data_h5_obj):
        if data_h5_obj:
            if isinstance(data_h5_obj, h5py.Group):
                for group_name in data_h5_obj.keys():
                    each_data = data_h5_obj[group_name]
                    if isinstance(each_data, np.ndarray):
                        print('np.ndarray')
                        cuttentnode1 = QTreeWidgetItem(node)
                        cuttentnode1.setText(0, str(group_name))
                        cuttentnode1.setText(1, str('np.ndarray'))
                        self.ProcessNpArray(each_data, node)
                    # data type is Dataset
                    elif isinstance(each_data, h5py.Dataset):
                        cuttentnode2 = QTreeWidgetItem(node)
                        cuttentnode2.setText(0, str(group_name))
                        cuttentnode2.setText(1, str(data_h5_obj[group_name]))
                        self.ProcessDataset(cuttentnode2, each_data)
                    # data type is Group
                    elif isinstance(each_data, h5py.Group):
                        cuttentnode3 = QTreeWidgetItem(node)
                        cuttentnode3.setText(0, str(group_name))
                        cuttentnode3.setText(1, str(data_h5_obj[group_name]))
                        self.ProcessGroup(cuttentnode3, each_data)
                    else:
                        print('unknown type')

    def ProcessDataset(self, node, data):
        data_value = data.value
        if isinstance(data_value, np.ndarray):
            self.ProcessNpArray(data_value, node)

    def ProcessNpArray(self, data_value, node):
        if data_value.shape.__len__() == 1:
            cuttentnode1 = QTreeWidgetItem(node)
            cuttentnode1.setText(0, str('np.ndarray1D'))
            cuttentnode1.setText(1, str(data_value.shape))
            cuttentnode1.setData(0, 1, data_value)
            # cuttentnode1.clicked.connect(self.ProcessArray1D(data_value))
            # cuttentnode1.itemClicked['QTreeWidgetItem*', 'int'].connect(self.ProcessArray1D(data_value))
        elif data_value.shape.__len__() == 2:
            cuttentnode2 = QTreeWidgetItem(node)
            cuttentnode2.setText(0, str('np.ndarray2D'))
            cuttentnode2.setText(1, str(data_value.shape))
            cuttentnode2.setData(0, 1, data_value)
            # cuttentnode2.itemClicked['QTreeWidgetItem*', 'int'].connect(self.ProcessArray2D(data_value))
            # self.ProcessArray2D(data_value)
        else:
            cuttentnode3 = QTreeWidgetItem(node)
            cuttentnode3.setText(0, str('np.ndarray'))
            cuttentnode3.setText(1, str(data_value.shape))
            cuttentnode3.setData(0, 1, data_value)
            # cuttentnode3.itemClicked['QTreeWidgetItem*', 'int'].connect(self.ProcessArray3D(data_value))
        # plt.imshow(data_np[2])
        # plt.show()

    def ProcessArray1D(self, data):
        print('1D clicked')
        tb = self.tableWidget
        tb.clear()
        data_len = data.shape[0]
        tb.setRowCount(1)
        tb.setColumnCount(data_len)
        for i, element in enumerate(data):
            # print(i)
            # print(element)
            # print('--------')
            tb.setItem(0, i, QTableWidgetItem(str(element)))

    def ProcessArray2D(self, data):
        print('2D clicked')

    def ProcessArray3D(self, data):
        print('3D clicked')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = h5ReaderConnection()
    win.show()
    sys.exit(app.exec_())

