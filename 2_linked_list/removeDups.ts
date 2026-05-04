import { NodeLinked } from "./LinkedList";

function removeDups(list: NodeLinked) {
  const CONTAINER = new Set();

  let currentNode: NodeLinked | null = list;

  let previousNode = currentNode;

  while (currentNode !== null) {
    if (CONTAINER.has(currentNode.data)) {
      previousNode.next = currentNode.next;
    }

    CONTAINER.add(currentNode.data);

    previousNode = currentNode;
    currentNode = currentNode.next;
  }
}

// Don't use buffer

// O(n²) time but O(1) space
function removeDupsNotBuffer(list: NodeLinked) {
  let currentNode: NodeLinked | null = list;

  while (currentNode !== null) {
    let runner = currentNode;

    while (runner.next !== null && currentNode) {
      if (currentNode && runner.next.data === currentNode.data) {
        runner.next = runner.next.next;
      } else {
        runner = runner.next;
      }
    }

    currentNode = currentNode.next;
  }
}

let L: NodeLinked | null = new NodeLinked(1);

L = L.appendToTail(2);

L = L.appendToTail(3);

L = L.appendToTail(1);

L = L.appendToTail(5);

L = L.appendToTail(2);

if (L) L.printList();

removeDups(L);

L.printList();

console.log("Teste segunda função");

let lista_2: NodeLinked | null = new NodeLinked(1);

lista_2 = lista_2.appendToTail(2);

lista_2 = lista_2.appendToTail(3);

lista_2 = lista_2.appendToTail(1);

lista_2 = lista_2.appendToTail(5);

lista_2 = lista_2.appendToTail(2);

if (lista_2) lista_2.printList();

removeDupsNotBuffer(lista_2);

lista_2.printList();
