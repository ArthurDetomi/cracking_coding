import { NodeLinked } from "./LinkedList";

function deleteMiddle(node: NodeLinked | null) {
  if (node === null || node.next === null) {
    return false;
  }

  let next = node.next;
  node.data = next.data;
  node.next = next.next;

  return true;
}

let L: NodeLinked | null = new NodeLinked(1);

L = L.appendToTail(2);

L = L.appendToTail(3);

L = L.appendToTail(5);

L = L.appendToTail(2);

L = L.appendToTail(3);

L = L.appendToTail(5);

deleteMiddle()
