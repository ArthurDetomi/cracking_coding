import { NodeLinked } from "./LinkedList";

function printKthToLast(head: NodeLinked | null, k: number) {
  if (head === null) {
    return 0;
  }

  let index: number = printKthToLast(head.next, k) + 1;

  if (index === k) {
    console.log(k + " th to last node is " + head.data);
  }

  return index;
}

function nthToLast(head: NodeLinked | null, k: number) {
  let p1: NodeLinked | null = head;
  let p2: NodeLinked | null = head;

  for (let i = 0; i < k; i++) {
    if (p1 === null) return null;

    p1 = p1.next;
  }

  while (p1 !== null) {
    if (p2 !== null) p2 = p2.next;
    p1 = p1.next;
  }

  return p2;
}

let L: NodeLinked | null = new NodeLinked(1);

L = L.appendToTail(2);

L = L.appendToTail(3);

L = L.appendToTail(5);

let index = 2;

console.log(nthToLast(L, index));

printKthToLast(L, index);
