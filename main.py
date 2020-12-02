import networkx as nx
import matplotlib.pyplot as plt
import random as random
import xlsxwriter


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


def compute_graph_instance(no_of_nodes, p, row, worksheet):
    g = nx.Graph()
    g.add_nodes_from(range(1, no_of_nodes + 1))
    nodeDegrees = [0] * no_of_nodes;
    for i in range(1, noOfNodes + 1):
        for j in range(i + 1, no_of_nodes + 1):
            if random.random() <= p:
                g.add_edge(i, j)
                nodeDegrees[i - 1] = nodeDegrees[i - 1] + 1;
                nodeDegrees[j - 1] = nodeDegrees[j - 1] + 1;
            else:
                continue

    # nx.draw(G, ,with_labels=False)
    pos = nx.spring_layout(g)
    nx.draw_networkx_nodes(g, pos=pos, node_size=10)
    nx.draw_networkx_edges(g, pos)
    fileName = "graph_instance_" + str(row) + ".png"
    plt.savefig(fileName)
    plt.close()
    # plt.show()
    write_edge_values(worksheet, row, noOfNodes, probability, g)
    write_edge_degree_values(worksheet, row, noOfNodes, probability, nodeDegrees)


def write_edge_values(worksheet, row, no_of_nodes, p, graph):
    expected_edges = no_of_nodes * (no_of_nodes - 1) * p / 2
    actual_edge = graph.number_of_edges()

    worksheet.write(row, 0, expected_edges)
    worksheet.write(row, 1, actual_edge)
    # print("ExpectedActualEdge ratio -> " + str(expectedEdges) + ":" + str(actualEdge))


def write_edge_degree_values(worksheet, row, no_of_nodes, p, node_degrees):
    expected_node_degeree = no_of_nodes * p

    node_degree_sum = 0
    for i in range(1, no_of_nodes + 1):
        node_degree_sum = node_degree_sum + node_degrees[i - 1]

    actual_node_degree = node_degree_sum / no_of_nodes
    worksheet.write(row, 2, expected_node_degeree)
    worksheet.write(row, 3, actual_node_degree)
    # print("Expected Vs Actual - Average node Degree ->" + str(expectedNodeDegeree) + ":" + str(actualNodeDegree))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    noOfNodes = int(input("Enter the No. of Nodes: "))
    probability = float(input("Enter probability: "))
    noOfGraphInstances = int(input("No. of graph instances needed: "))

    workbook = xlsxwriter.Workbook('Sample_G_n_p_output.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "n");
    worksheet.write(0, 1, "p");
    worksheet.write(0, 2, "Total Graph instances computed");
    worksheet.write(1, 0, noOfNodes);
    worksheet.write(1, 1, probability);
    worksheet.write(1, 2, noOfGraphInstances)

    worksheet.write(2, 0, "Expected Vs Actual Property comparison")

    worksheet.write(3, 0, "Expected number of Edges")
    worksheet.write(3, 1, "Actual number of Edges")

    worksheet.write(3, 2, "Expected average node degree")
    worksheet.write(3, 3, "Actual average node degree")

    row = 4
    for i in range(1, noOfGraphInstances+1):
        compute_graph_instance(noOfNodes, probability, row, worksheet)
        row = row + 1

    for i in range(4, noOfGraphInstances + 4):
        row = row + 3
        worksheet.write(row, 0, "Graph Instance" + str(i-3) + ":")
        row = row + 2
        worksheet.insert_image(row, 0, "graph_instance_" + str(i) + ".png")
        row = row + 24

    workbook.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
