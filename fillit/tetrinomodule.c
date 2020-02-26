/*
https://docs.python.org/3/extending/extending.html
*/

#include <stdlib.h>
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <unistd.h>
#include <fcntl.h>
#include "fillit.h"

char *grid_result(const char *file)
{
	int					fd;
	t_tetrino			*lst_ttx;
	static t_grid		*grid = NULL;

	fd = open(file, O_RDONLY);
	if (fd == -1)
		return ("");
	lst_ttx = ft_fillit_reader(fd);
	if (lst_ttx == NULL)
		return ("");
	if (grid != NULL)
		free(grid);
	grid = init_grid(lst_ttx);
	if (grid == NULL)
		return ("");
	if (!resolve_iter2(grid))
    {
        delete_list_tetrino(&lst_ttx);
		return ("");
    }
	delete_list_tetrino(&lst_ttx);
    grid->table2[grid->sq_size] = '\0';
	return (grid->table2);
}

static PyObject *tetrino_system(PyObject *self, PyObject *args)
{
    const char *command;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    char *sts = grid_result(command);
    return Py_BuildValue("s", sts);
}

static PyMethodDef TetrinoMethods[] = {
    {"resolve", tetrino_system, METH_VARARGS, "Python call to tetrino"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef tetrinomodule = {
    PyModuleDef_HEAD_INIT,
    "tetrino",
    "Python interface for tetrino",
    -1,
    TetrinoMethods
};

PyMODINIT_FUNC PyInit_tetrino(void) {
    return PyModule_Create(&tetrinomodule);
}
