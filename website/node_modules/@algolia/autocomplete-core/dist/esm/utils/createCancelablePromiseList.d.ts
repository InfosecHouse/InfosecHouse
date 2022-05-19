import { CancelablePromise } from '.';
export declare type CancelablePromiseList<TValue> = {
    add(cancelablePromise: CancelablePromise<TValue>): CancelablePromise<TValue>;
    cancelAll(): void;
    isEmpty(): boolean;
};
export declare function createCancelablePromiseList<TValue>(): CancelablePromiseList<TValue>;
